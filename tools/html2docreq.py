"""Usage: python3 -I html2docreq.py <html> <current_end_index> <out.json>
Builds a Docs batchUpdate: delete body, insert plain text, then heading/bold/italic/link/bullet styles."""
import sys, json, re
from html.parser import HTMLParser
src, end, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.paras=[]; s.cur=None; s.skip=0; s.fmt=[]; s.href=None; s.depth=0; s.olcount=[]
    def start_para(s, kind, level=0):
        s.flush(); s.cur={'kind':kind,'level':level,'text':'','spans':[]}
    def flush(s):
        if s.cur and s.cur['text'].strip():
            t=s.cur['text']; l=len(t)-len(t.lstrip()); s.cur['text']=t.strip()
            s.cur['spans']=[(a-l,b-l,k,v) for a,b,k,v in s.cur['spans']]
            s.paras.append(s.cur)
        s.cur=None
    def handle_starttag(s, tag, attrs):
        a=dict(attrs)
        if tag in ('style','title','head'): s.skip+=1
        elif tag=='h1': s.start_para('H1')
        elif tag=='h2': s.start_para('H2')
        elif tag=='h3': s.start_para('H3')
        elif tag in ('ul','ol'): s.depth+=1; s.olcount.append(0 if tag=='ol' else None)
        elif tag=='li':
            if s.olcount and s.olcount[-1] is not None: s.olcount[-1]+=1
            s.start_para('LI', s.depth)
            if s.olcount and s.olcount[-1] is not None: s.cur['text']+=f"{s.olcount[-1]}. "
        elif tag in ('p','div'): s.start_para('P')
        elif tag=='br':
            if s.cur: s.flush(); s.start_para('P')
        elif tag in ('b','strong','i','em','a','code','span'):
            if s.cur is None: s.start_para('P')
            s.fmt.append((tag, len(s.cur['text']), a.get('href')))
    def handle_endtag(s, tag):
        if tag in ('style','title','head'): s.skip-=1
        elif tag in ('h1','h2','h3','p','div'): s.flush()
        elif tag=='li': s.flush()
        elif tag in ('ul','ol'): s.flush(); s.depth-=1; s.olcount.pop()
        elif tag in ('b','strong','i','em','a','code','span') and s.fmt:
            t,st,href=s.fmt.pop()
            if s.cur is None: return
            en=len(s.cur['text'])
            k={'b':'bold','strong':'bold','i':'italic','em':'italic','a':'link','code':'code','span':'bold'}[t]
            s.cur['spans'].append((st,en,k,href))
    def handle_data(s, d):
        if s.skip: return
        d=re.sub(r'\s+',' ',d)
        if not d.strip() and (s.cur is None or not s.cur['text']): return
        if s.cur is None: s.start_para('P')
        s.cur['text']+=d
p=P(); p.feed(open(src,encoding='utf-8').read()); p.flush()
u=lambda x: len(x.encode('utf-16-le'))//2
text=''; pos=[]
for q in p.paras:
    q['text']=re.sub(r' +',' ',q['text'])
    pos.append(1+u(text)); text+=q['text']+'\n'
req=[{"deleteContentRange":{"range":{"startIndex":1,"endIndex":end-1}}},
     {"insertText":{"location":{"index":1},"text":text}}]
total=1+u(text)
req.append({"updateParagraphStyle":{"range":{"startIndex":1,"endIndex":total},"paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}})
req.append({"updateTextStyle":{"range":{"startIndex":1,"endIndex":total-1},"textStyle":{},"fields":"bold,italic,link"}})
bul=[]
for q,s0 in zip(p.paras,pos):
    e0=s0+u(q['text'])
    st={'H1':'HEADING_1','H2':'HEADING_2','H3':'HEADING_3'}.get(q['kind'])
    if st: req.append({"updateParagraphStyle":{"range":{"startIndex":s0,"endIndex":e0+1},"paragraphStyle":{"namedStyleType":st},"fields":"namedStyleType"}})
    for a,b,k,v in q['spans']:
        a=max(0,a); b=min(len(q['text']),b)
        if b<=a: continue
        ra=s0+u(q['text'][:a]); rb=s0+u(q['text'][:b])
        if k=='bold': ts,f={"bold":True},"bold"
        elif k=='italic': ts,f={"italic":True},"italic"
        elif k=='link' and v: ts,f={"link":{"url":v}},"link"
        elif k=='code': ts,f={"weightedFontFamily":{"fontFamily":"Roboto Mono"}},"weightedFontFamily"
        else: continue
        req.append({"updateTextStyle":{"range":{"startIndex":ra,"endIndex":rb},"textStyle":ts,"fields":f}})
# bullet glyphs: prefix LI paragraphs without numbers by inserting via createParagraphBullets on contiguous LI runs
runs=[];cur=None
for q,s0 in zip(p.paras,pos):
    e0=s0+u(q['text'])
    if q['kind']=='LI' and not re.match(r'\d+\. ',q['text']):
        if cur and cur[1]==s0-1: cur[1]=e0
        else:
            cur=[s0,e0]; runs.append(cur)
    else: cur=None
for a,b in runs:
    req.append({"createParagraphBullets":{"range":{"startIndex":a,"endIndex":b},"bulletPreset":"BULLET_DISC_CIRCLE_SQUARE"}})
for q,s0 in zip(p.paras,pos):
    if q['kind']=='LI' and q['level']>=2:
        e0=s0+u(q['text']); ind=36*(q['level']-1)+18
        req.append({"updateParagraphStyle":{"range":{"startIndex":s0,"endIndex":e0+1},"paragraphStyle":{"indentStart":{"magnitude":ind,"unit":"PT"},"indentFirstLine":{"magnitude":ind-18,"unit":"PT"}},"fields":"indentStart,indentFirstLine"}})
json.dump(req,open(out,'w'),ensure_ascii=False)
print(len(p.paras),'paras',len(req),'requests',len(json.dumps(req)),'bytes; text units',u(text))
