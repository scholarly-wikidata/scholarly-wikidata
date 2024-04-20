import json
from preface_utils import get_file_names
from llm_utils import get_important_dates

if __name__ == "__main__":
    file_names = get_file_names("data/eswc/web_crawl")
    file_names = sorted([f_name for f_name in file_names if f_name.endswith("_crawled_pages_filteredText.json")])
    
    with open("data/eswc/important_dates/important_dates_gpt-4-turbo-preview.txt", "w") as output, \
            open("data/eswc/important_dates/important_dates_gpt-4-turbo-preview.csv", "w", buffering=1) as out_csv:
        out_csv.write("conf_id, track, activity, date, reference_url\n")
        for f_name in file_names:
            conf_name = f_name.replace("data/eswc/web_crawl/", "").replace("_crawled_pages_filteredText.json", "")
            output.write(f"=============== {conf_name} ===============\n\n")
            with open(f_name) as in_file:
                json_data = json.load(in_file)

            for page_key in json_data:
                page_text = json_data[page_key]
                if "call for paper" in page_text["title"].lower() or "important date" in page_text["text"].lower() or "call for paper" in page_text["title"].lower() or "important date" in page_text["text"].lower():
                    important_dates_text = "Page URL: " + page_key + "\n\n"
                    important_dates_text += "Page title: " + page_text["title"] + "\n\n" + "Page content:" + page_text["text"] + "\n\n"
                    output.write(important_dates_text)
                    important_dates = get_important_dates(important_dates_text)
                    important_dates = important_dates.replace("--- complete ----","")
                    output.write("Output: \n")
                    output.write(important_dates)
                    important_dates = important_dates.replace("track, activity, date", "")
                    important_dates = "\n".join([f"{conf_name},{line},{page_key}" for line in important_dates.split("\n") 
                                                 if len(line.split(",")) > 2])
                    out_csv.write(f"{important_dates}\n")

        



