import langchain
from preface_utils import get_file_names, get_oc_content
from llm_utils import get_oc_member_roles

if __name__ == "__main__":
    langchain.debug = False
    pdf_files = get_file_names("data/iswc/preface")
    pdf_files = sorted(pdf_files)
    with open("data/iswc/acceptance/iswc_oc_role_gpt-4-turbo-preview.txt", "w", buffering=1) as out_file, \
        open("data/iswc/acceptance/iswc_oc_role_gpt-4-turbo-preview.csv", "w", buffering=1) as out_csv:
        for file_path in pdf_files:
            conf_name = f"{file_path.replace('data/iswc/preface/', '').replace('.pdf', '')}\n".upper().strip()
            out_file.write(f"===========  {conf_name}  ===========\n")
            preface_oc_content = get_oc_content(file_path)
            out_file.write(f"Evidence:\n{preface_oc_content}\n\n")
            try:
                llm_output = get_oc_member_roles(preface_oc_content)
                llm_output = llm_output.replace("--- complete ----", "").strip()
                for line in llm_output.split("\n"):
                    out_csv.write(f"{conf_name},{line.strip()}\n")
            except Exception as ex:
                continue
            out_file.write("Output:\n")
            out_file.write(llm_output)
            out_file.write("\n\n")
