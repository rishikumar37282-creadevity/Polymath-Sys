import os
import re

html_files = [
    r"c:\Users\ayush\OneDrive\Desktop\Subject\Eng\AI Research Eng\phase1_learning_roadmap.html", 
    r"c:\Users\ayush\OneDrive\Desktop\Subject\Eng\AI Research Eng\phase2_deep_roadmap.html", 
    r"c:\Users\ayush\OneDrive\Desktop\Subject\Eng\AI Research Eng\phase3_frontier_roadmap.html"
]

ICONS = {
    '▶': '<svg class="res-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>',
    '📖': '<svg class="res-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>',
    '🏆': '<svg class="res-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>',
    '📄': '<svg class="res-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>',
    '🛠': '<svg class="res-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>',
    '🃏': '<svg class="res-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>',
    '📝': '<svg class="res-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>',
    '✅': '<svg class="res-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>'
}

LINKS = {
    "3Blue1Brown — Essence of Linear Algebra": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab",
    "MIT 18.06 — Gilbert Strang (OCW)": "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/",
    "Harvard Stat110 — Joe Blitzstein": "https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo",
    "StatQuest with Josh Starmer": "https://www.youtube.com/@statquest",
    "Think Bayes + Think Stats": "https://greenteapress.com/wp/",
    "3Blue1Brown — Essence of Calculus": "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
    "NeetCode.io": "https://neetcode.io/",
    "Abdul Bari — Algorithms": "https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O",
    "Visualgo.net": "https://visualgo.net/",
    "Amigoscode — Spring Boot": "https://www.youtube.com/watch?v=9SGDpanrc8U",
    "ByteByteGo — System Design": "https://www.youtube.com/@ByteByteGo",
    "Python Data Science Handbook": "https://jakevdp.github.io/PythonDataScienceHandbook/",
    "Corey Schafer — Python + Pandas": "https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDZAskcbF7i",
    "Andrew Ng — ML Specialization": "https://www.coursera.org/specializations/machine-learning-introduction",
    "Kaggle competitions": "https://www.kaggle.com/competitions",
    "fast.ai — Practical Deep Learning": "https://course.fast.ai/",
    "Karpathy — Neural Networks": "https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ",
    "Andrej Karpathy — Neural Networks": "https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ",
    "Deep Learning Specialization — Andrew Ng": "https://www.coursera.org/specializations/deep-learning",
    "Andrej Karpathy — \"Let's build GPT\"": "https://www.youtube.com/watch?v=kCc8FmEb1nY",
    "Karpathy — Let's build GPT": "https://www.youtube.com/watch?v=kCc8FmEb1nY",
    "\"Attention Is All You Need\"": "https://arxiv.org/abs/1706.03762",
    "DeepLearning.ai short courses": "https://www.deeplearning.ai/short-courses/",
    "fast.ai Part 2": "https://course.fast.ai/",
    "Deep Learning with PyTorch": "https://pytorch.org/assets/deep-learning/Deep-Learning-with-PyTorch.pdf",
    "PyTorch official tutorials": "https://pytorch.org/tutorials/",
    "Build a Large Language Model from Scratch": "https://github.com/rasbt/LLMs-from-scratch",
    "Core papers to read in sequence": "https://arxiv.org/abs/1706.03762",
    "DeepLearning.ai — Building and Evaluating Advanced RAG": "https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/",
    "LangChain + LlamaIndex official docs": "https://python.langchain.com/",
    "DeepLearning.ai — Functions, Tools and Agents": "https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/",
    "LangGraph documentation": "https://langchain-ai.github.io/langgraph/",
    "HuggingFace NLP Course": "https://huggingface.co/learn/nlp-course/",
    "Made With ML": "https://madewithml.com/",
    "Full Stack Deep Learning": "https://fullstackdeeplearning.com/",
    "Weights & Biases free courses": "https://wandb.ai/courses",
    "ML System Design — 300 case studies": "https://github.com/eugeneyan/applied-ml",
    "Learn Quantum Computation using Qiskit": "https://learn.qiskit.org/",
    "IBM Quantum Learning": "https://learning.quantum.ibm.com/",
    "PennyLane documentation": "https://pennylane.ai/qml/",
    "Qiskit Finance module": "https://qiskit.org/ecosystem/finance/",
    "Andrew Ng — How to read research papers": "https://www.youtube.com/watch?v=733m6qBH-jI",
    "Papers With Code": "https://paperswithcode.com/",
    "Yannic Kilcher": "https://www.youtube.com/@YannicKilcher",
    "The Craft of Research": "https://press.uchicago.edu/ucp/books/book/chicago/C/bo23521678.html",
    "How to write a great research paper": "https://www.youtube.com/watch?v=VK51E_gRNkk",
    "Visual Complex Analysis": "https://en.wikipedia.org/wiki/Visual_Complex_Analysis"
}

ARCH_INSERTS = {
    'phase1_learning_roadmap.html': {
        'id="p5"': '<a href="architectures/rag_pipeline.md" class="arch-btn" target="_blank"><span style="display:flex;align-items:center;gap:8px;"><svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg> View RAG Architecture Interactive Diagram</span><span>&rarr;</span></a>\n    <div class="track-header">'
    },
    'phase2_deep_roadmap.html': {
        'id="p1"': '<a href="architectures/transformer.md" class="arch-btn" target="_blank"><span style="display:flex;align-items:center;gap:8px;"><svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg> View Transformer Architecture Interactive Diagram</span><span>&rarr;</span></a>\n  <div class="sec">'
    },
    'phase3_frontier_roadmap.html': {
         'id="p2"': '<a href="architectures/qml_architecture.md" class="arch-btn" target="_blank"><span style="display:flex;align-items:center;gap:8px;"><svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg> View QML Variational Circuit Diagram</span><span>&rarr;</span></a>\n  <div class="sec-label">'
    }
}

for fname in html_files:
    if not os.path.exists(fname):
        print(f"Skipping {fname}, does not exist")
        continue

    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply Icon SVGs
    for emoji, svg in ICONS.items():
        content = content.replace(f'<div class="res-icon">{emoji}</div>', f'<div class="res-icon">{svg}</div>')
        content = content.replace(f'<div class="rico">{emoji}</div>', f'<div class="rico">{svg}</div>')

    def replace_links(split_str, content):
        parts = content.split(split_str)
        for i in range(1, len(parts)):
            if parts[i].startswith('<a '):
                # already linked!
                continue
                
            end_idx = parts[i].find('</div>')
            if end_idx != -1:
                div_content = parts[i][:end_idx]
                text_part = div_content.split('<span')[0].strip()
                
                matched_url = None
                for kw, url in LINKS.items():
                    if kw in text_part:
                        matched_url = url
                        break
                
                if matched_url:
                    new_text_part = f'<a href="{matched_url}" target="_blank" class="res-link">{text_part} <span class="res-link-arrow">&nearr;</span></a> '
                    rest_part = div_content[len(text_part):]
                    parts[i] = new_text_part + rest_part + parts[i][end_idx:]
        return split_str.join(parts)

    content_old = content
    content = replace_links('<div class="res-name">', content)
    content = replace_links('<div class="rname">', content)

    # Inject arch
    base_name = os.path.basename(fname)
    if base_name in ARCH_INSERTS:
        for k, v in ARCH_INSERTS[base_name].items():
            if base_name == "phase1_learning_roadmap.html":
                content = content.replace(f'<div class="panel" {k}>\n    <div class="track-header">', f'<div class="panel" {k}>\n    {v}\n    <div class="track-header">')
            else:
                content = content.replace(f'<div class="panel" {k}>\n  <div class="sec">', f'<div class="panel" {k}>\n  {v}\n  <div class="sec">')
                content = content.replace(f'<div class="panel" {k}>\n  <div class="sec-label">', f'<div class="panel" {k}>\n  {v}\n  <div class="sec-label">')

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated all HTMLs")
