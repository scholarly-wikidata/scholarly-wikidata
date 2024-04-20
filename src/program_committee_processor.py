
from preface_utils import get_file_names, get_pc_content
import pandas as pd

key_to_track = {
    "research" : "Q125208100",
    "resource": "Q125364239",
    "in-use": "Q125364246"
}

key_to_role = {
    "member": "Q9200127",
    "senior member": "Q125364314"
}

def create_df(path, role, track):
    df = pd.read_csv(path)
    df['status'] = key_to_role[role]
    df['track'] = key_to_track[track]
    df.columns = ["Name", "Role", "Track"]
    return df

def generate_excel(year):
    inputs = [
        [f"data/iswc/oc/{year}/Research_Track_Senior_Program_Committee.csv", "senior member", "research"],
        [f"data/iswc/oc/{year}/Research_Track_Program_Committee.csv", "member", "research"],
        [f"data/iswc/oc/{year}/Resources_Track_Senior_Program_Committee.csv","senior member", "resource"],
        [f"data/iswc/oc/{year}/Resources_Track_Program_Committee.csv", "member", "resource"],
        [f"data/iswc/oc/{year}/In-Use_Track_Program_Committee.csv", "member", "in-use"]
    ]

    df = pd.DataFrame()
    for pc_in in inputs:
        t_df = create_df(pc_in[0], pc_in[1], pc_in[2])
        df = pd.concat([df, t_df])
    df['Name String'] = df['Name']
    df = df.reset_index(drop=True)
    df.to_excel(f"data/iswc/oc/{year}/iswc_{year}_pc_members.xlsx")

def generate_csvs():
    pdf_files = get_file_names("data/iswc/preface")
    pdf_files = sorted(pdf_files)
    print(pdf_files[-11:-10])
    for file_path in pdf_files[-11:-10]:
        conf_name = file_path.rsplit("/",2)[2].replace(".pdf","").upper().strip()
        print(f"===========  {conf_name}  ===========\n")
        oc_to_people = get_pc_content(file_path)
        for oc_key in oc_to_people:
            with open(f"data/iswc/pc/2013/{conf_name}_{oc_key.replace(' ', '_')}.csv", "w") as out_file:
                for line in oc_to_people[oc_key]:
                    out_file.write(f"{line}\n")


if __name__ == "__main__":

    generate_csvs()
    #generate_excel("2022")
