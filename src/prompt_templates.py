stop_sequence = "--- complete ----"

acceptance_ratio_prompt_template = """You are a data entry clerk and you know how to read some text and
extract the requested information. You always follow the expected output format shown in the examples precisely.
You only extract information in the text and do not introduce any new facts.

Given a preface from a conference proceedings, extract the number of research papers submitted and accepted to each
track. Output the results in the CSV format.

Here are two examples:

Preface: The main scientiﬁc program of ESWC 2023 contained 41 papers selected out of 167 submissions
(98 research, 23 in-use, 46 resource): 19 papers in the research track, 9 in the in-use track, and 13 in the resource
track. The overall acceptance rate was 24% (19% research, 39% in-use, 28% resource).

Output:
track, submitted, accepted
research, 98, 19
in-use, 23, 9
resource, 46, 13
--- complete ----

Preface: The research papers program received 245 full paper submissions, which were ﬁrst evaluated by the Program
Committees of the respective tracks. The review process included evaluation by Program Committee members, discussions to
resolve conﬂicts, and a metareview for each potentially acceptable borderline submission.After this a physical meeting
among Track and Conference Chairs was organized to see that comparable evaluation criteria in diﬀerent tracks had
been used and to discuss remaining borderline papers.As a result, 52 research papers were selected to be presented at
the conference. The proceedings also include ten PhD symposium papers presented at a separate track preceding the main
conference, and 17 demo papers giving a brief description of the system demos that were accepted for presentation in a
dedicated session during the conference.

Output:
track, submitted, accepted
research, 245, 52
PhD symposium, - , 10
demo, - , 17
--- complete ----

Now extract the number of research papers submitted and accepted to each track from the following text. Output only the
CSV content and "--- complete ----" as the last line.

Preface: {preface_text}

Output:
track, submitted, accepted
"""

acceptance_ratio_system_template = """You are a data entry clerk and you know how to read some text and
extract the requested information. You always follow the expected output format shown in the examples precisely.
You only extract information in the text and do not introduce any new facts."""

acceptance_ratio_human_template = """Given a preface from a conference proceedings, extract the number of research papers submitted and accepted to each
track. Output the results in the CSV format.

Here are two examples:

Preface: The main scientiﬁc program of ESWC 2023 contained 41 papers selected out of 167 submissions
(98 research, 23 in-use, 46 resource): 19 papers in the research track, 9 in the in-use track, and 13 in the resource
track. The overall acceptance rate was 24% (19% research, 39% in-use, 28% resource).

Output:
track, submitted, accepted
research, 98, 19
in-use, 23, 9
resource, 46, 13
--- complete ----

Preface: The research papers program received 245 full paper submissions, which were ﬁrst evaluated by the Program
Committees of the respective tracks. The review process included evaluation by Program Committee members, discussions to
resolve conﬂicts, and a metareview for each potentially acceptable borderline submission.After this a physical meeting
among Track and Conference Chairs was organized to see that comparable evaluation criteria in diﬀerent tracks had
been used and to discuss remaining borderline papers.As a result, 52 research papers were selected to be presented at
the conference. The proceedings also include ten PhD symposium papers presented at a separate track preceding the main
conference, and 17 demo papers giving a brief description of the system demos that were accepted for presentation in a
dedicated session during the conference.

Output:
track, submitted, accepted
research, 245, 52
PhD symposium, - , 10
demo, - , 17
--- complete ----

Now extract the number of research papers submitted and accepted to each track from the following text. Output only the
CSV content and "--- complete ----" as the last line.

Preface: {preface_text}

Output:
track, submitted, accepted
"""

oc_role_extraction_template =  """You are a data entry clerk and you know how to read some text and
extract the requested information. You always precisely follow the expected output format shown in the examples.
You only extract information in the text and do not introduce any new facts.

Your task is to extract the names of the organization committe with their roles given a preface from a conference proceedings. Output the results in the CSV format.

Here are two examples:

Preface:
General Chair
Steffen Staab Universit ät Koblenz-Landau, Germany
Local Chair
Jeff He ﬂin Lehigh University, USA
Sponsorship Chairs
Michelle Cheatham Wright State University, USACarlos Pedrinaci The Open University, UK
Metadata Chair
Heiko Paulheim University of Mannheim, Germany
Publicity Chair
Juan Sequeda Capsenta Labs, USA

Output:
general chair, Steffen Staab
local chair, Jeff He ﬂin
sponsorship chair, Michelle Cheatham
sponsorship chair, Carlos Pedrinaci
metadata chair, Heiko Paulheim
publicity chair, Juan Sequeda
--- complete ----

Preface:
Organization
Organizing Committee
General Chair
Chris Welty IBM Research, USA
Vice Chair
Dimitrios Georgakopoulos CSIRO, Australia
Publicity Chairs
Armin Haller CSIRO, Australia
Yuan-Fang Li Monash University, Australia
Kingsley Idehen OpenLink Software, USA
Proceedings Chair
Krzysztof Janowicz University of California, Santa Barbara, US

Output:
general chair, Chris Welty
vice chair, Dimitrios Georgakopoulos
publicity chair, Armin Haller
publicity chair, Yuan-Fang Li
publicity chair, Kingsley Idehen
proceedings chair, Krzysztof Janowicz
--- complete ----

Now extract the names and the roles of the organization committee members from the following text, Preface. Output only the
CSV content and write "--- complete ----" as the last line when you finish.

Preface: 
{preface_text}

Output:
"""


main_topics_extraction_template = """You are an expert researcher and you know how to extract information from a given text. You always precisely follow the expected output format shown in the examples.
You only extract information in the text and do not introduce any new facts.

Your task is read the preface of a conference and extract the main topics mentioned there. Output should be the list of topics, one each line without any additional text.

Here are two examples:

Preface: 
The workshops and tutorials program included a mix of established topics such as ontology matching, ontology design patterns, and semantics-powered data mining, as well as analytics alongside newer ones that reflect the commitment of the community to innovate and help create systems and technologies that people want and deserve, including semantic explainability or blockchain enabled Semantic Web. 

Topics:
ontology matching
ontology design patterns
semantics-powered data mining
semantic explainability
blockchain enabled Semantic Web
--- complete ----

Preface:
Eventually, new areas that are core to the Semantic Web field gain prominence as data and ontologies become more widespread on the Semantic Web, e.g., ontology evaluation (4), ontology reuse (4), searching and ranking ontologies (3), ontology extraction (2), and ontology evolution (1).

Topics:
ontology evaluation
ontology reuse
searching and ranking ontologies
ontology extraction
ontology evolution
--- complete ----

Now given following text from preface, please extract the main topics mentioned. Output only the topics, one each line and write "--- complete ----" as the last line when you finish.

Preface: 
{preface_text}

Topics:
"""


deadline_system_template = """You are a researcher who attends acadameic conferences. You follow instruct precisely and concise in your answers."""

deadline_human_template = """Given a snippet of text from the conference website, please extract the all important dates/deadlines for activities in each track. Examples of tracks are research, resoures, in-use, industry, semantic web challenges, tutorials, workshops, posters and demos, etc. Sometimes track is mentioned in the page title. Examples of activities are abstract submission, full paper submission, notification, camera-ready paper submission, etc. 

Important Dates:
track, activity, date
research track, abstract submission, 28 April 2022
research track, full paper submission, 	5 May 2022
posters and demo track, full paper submission, 	10 September 2022
resource track, notification, 7 July 2022
research track, camera-ready paper submission, 5 October 2022
"--- complete ----"

Please extract the all important dates/deadlines from the following text. Output only the CSV content using the above format and "--- complete ----" as the last line.

Website content: 
{website_text}

Important Dates:
"""

ner_person_system_template = """
You are an NLP researcher and you are an expert in detecting entities in next such as person names. You only extract names that are explicitly mentioned in text, nothing else.
"""

ner_person_human_template = """
Your task is to analyze the given Text and output the list of Names one each line. Print "--- complete ---" once you finish. Here are two example.

Text: Fajar J. Ekaputra Vienna University of Economics and Business,

Names: 
Fajar J. Ekaputra
--- complete ---

Text: Adila A. Krisnadhi Universitas Indonesia, IndonesiaMarkus Krötzsch TU Dresden, GermanyBenno Kruit Vrije Universiteit Amsterdam, The NetherlandsJose Emilio Labra Gayo Universidad de Oviedo, 
SpainAndré Lamurias Aalborg University, DenmarkAgnieszka Lawrynowicz Poznan University of Technology, PolandDanh Le Phuoc TU Berlin, GermanyMaxime Lefrançois Mines Saint-Étienne, 
FranceHuanyu Li Linköping University, SwedenTianyi Li University of Edinburgh, UKWenqiang Liu Tencent Inc., ChinaCarsten Lutz Universität Bremen, Germany

Names:
Adila A. Krisnadhi
Markus Krötzsch
Benno Kruit
Jose Emilio Labra Gayo
André Lamurias
Agnieszka Lawrynowicz
Danh Le Phuoc
Maxime Lefrançois
Huanyu Li
Tianyi Li
Wenqiang Liu
Carsten Lutz
--- complete ---

Now analyze the given Text and output the list of Names one each line. Print only the name in each line, don't add any other charactors. 
Text: {names_text}

Names:
"""