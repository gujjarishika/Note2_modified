from bs4 import BeautifulSoup
path = r"C:\Users\emb-rishguj\Downloads\Polysapce_CP_P3027-HVLSF_DeveloperReview.html"
with open(path,'r') as f:
    file=f.read()
    tree_obj=BeautifulSoup(file,"html.parser")
    table=False
    h1=False
    h2=False
    dictionary=dict()
    labels=list()
    for heading in tree_obj.find_all("h1"):
        if "Chapter" and "2" and "Polyspace Run-Time Checks Statistics" in heading.get_text():
            h1=True
            headings2 =heading.find_all_next("h2")
            for heading2 in headings2:
                if "Run-Time Checks Summary for Polysapce_CP_P3027-HVLSF - results" in heading2.get_text():
                    h2=True
                    table=heading2.find_next("table")
                    if table:
                        print("table found")
                        labels = [th.get_text(strip=True) for th in table.find("thead").find_all("td")]
                        print(labels)
                        no_of_rows=table.find("tbody").find_all("tr")
                        for row in no_of_rows:
                            row_text=[each_cell.get_text() for each_cell in row.find_all("td")]
                            if row_text:
                                row_dict={labels[i]:row_text[i] for i in range(1,len(labels))}
                                dictionary[row_text[0]]=row_dict
                        print(dictionary)
                        print(f"number of rows in the table are: {len(no_of_rows)}")
                    else:
                        print("table not found")
    if not h1:
        print("heading 1 is not found")
    elif h1 and not h2:
        print("heading 2 is not found")
    
    