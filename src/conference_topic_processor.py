import langchain
from preface_utils import get_file_names, get_preface_content
from llm_utils import get_conf_topics

if __name__ == "__main__":

    langchain.debug = False
    pdf_files = get_file_names("data/iswc/preface")
    pdf_files = sorted(pdf_files)
    with open("data/iswc/topic/iswc_topic_claude-3-opus-20240229.txt", "w", buffering=1) as out_file:
        for file_path in pdf_files:
            conf_name = f"{file_path.replace('data/iswc/', '').replace('.pdf', '')}\n".upper().strip()
            out_file.write(f"===========  {conf_name}  ===========\n")
            preface_content = get_preface_content(file_path)
            out_file.write(f"Evidence:\n{preface_content}\n\n")
            output = get_conf_topics(preface_content)
            output = output.replace("--- complete ----", "").strip()
            out_file.write(f"Output:\n{output}\n\n")
            out_file.write(f"Human Extraction:\ntrack, submitted, accepted\n\n")
            out_file.write(f"Eval Metrics:\nGold extractions: , Sys total: , Sys Correct: \n\n\n")