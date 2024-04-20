from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from os import listdir
from os.path import isfile, join
from collections import defaultdict
import re
import logging
from llm_utils import SBERTEmbeddings, get_name_list_from_text

logger = logging.getLogger()


pc_section_headers = ['Research Track Program Committee', 'Research Track Senior Program Committee', 'Research Track Additional Reviewers', 
                      'Research Track Senior Program Committee','Resources Track Senior Program Committee', 'Resources Track Program Committee', 'Resources Track Additional Reviewers', 'In-Use Track Program Committee', 'Senior Program Committee –Research Track', 'Program Committee –Research Track', 'Additional Reviewers –Research Track', 'In-Use Track Additional Reviewers', 'Senior Program Committee –Research Track', 'Program Committee –Resources Track', 'Additional Reviewers –Resources Track', 'Program Committee –In-Use Track', 'Additional Reviewers –In-Use Track', 'Senior Program Committee - Research Track', 'Program Committee - Research Track', 'Additional Reviewers - Research Track', 'Program Committee - Resources Track', 'Additional Reviewers - Resources Track', 'Program Committee - Applications Track', 'Additional Reviewers - Applications Track', 'Senior Program Committee: Research Track', 'Program Committee: Research Track',
                      'Additional Reviewers', 'Senior Program Committee – Research', 'Program Committee – Research', 'Additional Reviewers – Research', 'Senior Program Committee – Semantic Web In-Use', 'Program Committee – Semantic Web In-Use', 'Additional Reviewers – Semantic Web In-Use', 'Program Committee – Replication, Benchmark, Data and Software', 'Additional Reviewers – Replication, Benchmark, Data and Software', 'Program Committee – Doctoral Consortium']
pc_section_end = ['Sponsors']
oc_section_headers = ["Organization", "Conference Organization", "Conference Organisation", "Organizing Committee", "Programme Co-chairs, Research/Academic Track"]


def get_file_names(pdf_dir):
    pdf_files = [join(pdf_dir, f) for f in listdir(pdf_dir) if isfile(join(pdf_dir, f))]
    return pdf_files

def read_file_to_string(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

def get_preface_content(file_path: str):
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
    except Exception as ex:
        logger.error(f"error reading the file: {file_path} - {str(ex)}")
        raise ex
        
    preface_content = [page.page_content for page in pages]
    lines = []

    for page in preface_content:
        lines += page.split("\n")

    selected_content = ""
    include = False
    for line in lines:
        if line.strip().lower() == "preface":
            include = True
        if include and line.strip() in oc_section_headers:
            include = False
        if include:
            selected_content += line + "\n"

    return selected_content

def get_pc_content(file_path: str) -> dict:
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    preface_content = []
    for page in pages:
        preface_content += page.page_content.splitlines()
    current_section = None
    oc_to_people = defaultdict(list)
    for line in preface_content:
        if line.strip() in pc_section_headers:
            current_section = line.strip()
            continue
        if line.strip() in pc_section_end:
            break
        if current_section:
            names = get_name_list(line)
            oc_to_people[current_section] += names
    return oc_to_people


def get_name_list(name_content_text):

    orig_content = re.sub(r'\s+', '', name_content_text.lower())        
    names_list_text = get_name_list_from_text(name_content_text)
    names = []
    lines = names_list_text.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("*") or line.startswith("-"):
            line = line[1:]
        line = line.strip()
        if line == "" or "," in line:
            continue
        if len(line.split()) == 1:
            continue
        if re.sub(r'\s+', '', line.lower()) in orig_content:
            names.append(line)
    return names


def get_oc_content(file_path):
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
    except Exception as ex:
        logger.error(f"error reading the file: {file_path} - {str(ex)}")
        raise ex
        
    preface_content = [page.page_content for page in pages]
    lines = []

    for page in preface_content:
        lines += page.split("\n")

    selected_content = ""
    include = False
    for line in lines:
        if line.strip() in oc_section_headers:
            include = True
        if include and ("program committee" in line.lower() and "chair" not in line.lower()):
            include = False
        if include:
            selected_content += line + "\n"
    return selected_content

def get_acceptance_content(file_path):
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
    except Exception as ex:
        logger.error(f"error reading the file: {file_path} - {str(ex)}")
        raise ex
        
    preface_content = [page.page_content for page in pages]
    lines = []

    for page in preface_content:
        lines += page.split("\n")

    selected_content = ""
    include = False
    for line in lines:
        if line.strip().lower() == "preface":
            include = True
        if include and line.strip() in oc_section_headers:
            include = False
        if include:
            selected_content += line + "\n"
    lc_embeddings = SBERTEmbeddings()
    text_splitter = SemanticChunker(embeddings=lc_embeddings,
                                    breakpoint_threshold_type="percentile",
                                    breakpoint_threshold_amount=15)
    docs = text_splitter.create_documents([selected_content])
    filtered_content = ""
    keywords = ["submission", "paper", "accept", "submit", "poster", "demo", "phd", "track", 
                "doctoral", "consortium", "resource", "research", "in-use", "workshop", "tutorial"]
    for doc in docs:
        for keyword in keywords:
            if keyword in doc.page_content:
                filtered_content += doc.page_content
                break

    return filtered_content