import langchain
from preface_utils import get_file_names, get_acceptance_content
from llm_utils import get_acceptance_ratios

if __name__ == "__main__":

    langchain.debug = False
    pdf_files = get_file_names("data/eswc/preface")
    pdf_files = sorted(pdf_files)
    with open("data/eswc/acceptance/eswc_accept_ratio_claude-3-opus-20240229.txt", "w", buffering=1) as out_file:
        for file_path in pdf_files:
            conf_name = f"{file_path.replace('data/eswc/preface', '').replace('.pdf', '')}\n".upper().strip()
            out_file.write(f"===========  {conf_name}  ===========\n")
            preface_content = get_acceptance_content(file_path)
            out_file.write(f"Evidence:\n{preface_content}\n\n")
            retry_count = 0
            while retry_count < 10:
                output = get_acceptance_ratios(preface_content)
                output = output.replace("--- complete ----", "").strip()
                print(output)
                if "track, submitted, accepted" in output:
                    out_file.write(f"Output:\n{output}\n\n")
                    break
                else:
                    retry_count += 1
            out_file.write(f"Human Extraction:\ntrack, submitted, accepted\n\n")
            out_file.write(f"Eval Metrics:\nGold extractions: , Sys total: , Sys Correct: \n\n\n")






