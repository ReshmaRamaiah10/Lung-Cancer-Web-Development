#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
import json

cgitb.enable()


print("Content-type: text/html\n")

form = cgi.FieldStorage()

if (form):
    conn = pymysql.connect(host='bioed.bu.edu',
        user= 'Group_H',
        password= "Group_H",
        db= 'Group_H',
        port = 4253) 
    
    cur = conn.cursor()
    
    sample_type = form.getvalue("sample_type")
    year_of_diagnosis = form.getvalue("year_of_diagnosis")
    gender = form.getvalue("gender")
    prior_malignancy = form.getvalue("prior_malignancy")
    
    ajcc_pathologic_stage = form.getlist("ajcc_pathologic_stage")
    ajcc_staging_system_edition = form.getlist("ajcc_staging_system_edition")
    tissue_or_organ_of_origin = form.getlist("tissue_or_organ_of_origin")
    ajcc_pathologic_t = form.getlist("ajcc_pathologic_t")
    ajcc_pathologic_m = form.getlist("ajcc_pathologic_m")
    ajcc_pathologic_n = form.getlist("ajcc_pathologic_n")
    age_at_index = form.getlist("age_at_index")
    years_smoked = form.getlist("years_smoked")

    #Location = form.getlist("Location")
    
    query = ""
    
	query1 = """SELECT * 
	from TCGA_annotation ta
	inner join TCGA_whole_slide tws on left(tws.Sample_id, 30) = LEFT(ta.Sample_id, 30)"""
    
    query2 = """ SELECT * 
	from TCGA_annotation ta
	right join tcga_filtered_geneset tfg on tfg.sample_id = ta.Sample_id
	"""

    q1=q2=q3=q4=q5=q6=q7=q8=q9=q10=q11=q12= ""

    
    if sample_type is not None:
    	q1 = "SampleType == "
    	q1 += sample_type
    	l.append(q1)

    if year_of_diagnosis is not None:
    	q2 = "year_of_diagnosis == "
    	q2 += year_of_diagnosis
    	l.append(q2)

    if gender == "male":
    	q3 = "Genomic_Smoking_Status == male"
    	l.append(q3)

    elif status == "female":
    	q3 = "Genomic_Smoking_Status == female"
    	l.append(q3)
    
    if prior_malignancy == "yes":
    	q4 = "prior_malignancy == yes"
    	l.append(q4)

    elif prior_malignancy == "no":
    	q4 = "prior_malignancy == no"
    	l.append(q4)
    
    if len(ajcc_pathologic_stage) > 0 :
    	q5 = ""
    	if len(ajcc_pathologic_stage) == 1 :
    		q5 = "ajcc_pathologic_stage == "
    		q5 += ajcc_pathologic_stage[0]
    	else :
    		for i in ajcc_pathologic_stage[:-1]:
    			q = "(ajcc_pathologic_stage == "
    			q += i
    			q += " OR "
    			q7 += q
    		q = "ajcc_pathologic_stage =="
    		q += ajcc_pathologic_stage[-1]
    		q += ")"
    		q5 += q
    	l.append(q5)
    
    if len(ajcc_staging_system_edition) > 0 :
    	q6 = ""
    	if len(ajcc_staging_system_edition) == 1 :
    		q6 = "ajcc_staging_system_edition == "
    		q6 += ajcc_staging_system_edition[0]
    	else :
    		for i in ajcc_staging_system_edition[:-1]:
    			q = "(ajcc_staging_system_edition == "
    			q += i
    			q += " OR "
    			q6 += q
    		q = "ajcc_staging_system_edition =="
    		q += ajcc_staging_system_edition[-1]
    		q += ")"
    		q6 += q
    	l.append(q6)

    if len(tissue_or_organ_of_origin) > 0 :
    	q7 = ""
    	if len(tissue_or_organ_of_origin) == 1 :
    		q7 = "tissue_or_organ_of_origin == "
    		q7 += tissue_or_organ_of_origin[0]
    	else :
    		for i in tissue_or_organ_of_origin[:-1]:
    			q = "(tissue_or_organ_of_origin == "
    			q += i
    			q += " OR "
    			q7 += q
    		q = "tissue_or_organ_of_origin =="
    		q += tissue_or_organ_of_origin[-1]
    		q += ")"
    		q7 += q
    	l.append(q7)
    	
    if len(ajcc_pathologic_t) > 0 :
    	q8 = ""
    	if len(ajcc_pathologic_t) == 1 :
    		q8 = "ajcc_pathologic_t == "
    		q8 += ajcc_pathologic_t[0]
    	else :
    		for i in ajcc_pathologic_t[:-1]:
    			q = "(ajcc_pathologic_t == "
    			q += i
    			q += " OR "
    			q8 += q
    		q = "ajcc_pathologic_t =="
    		q += ajcc_pathologic_t[-1]
    		q += ")"
    		q8 += q
    	l.append(q8)
    	
    if len(ajcc_pathologic_m) > 0 :
    	q9 = ""
    	if len(ajcc_pathologic_m) == 1 :
    		q9 = "ajcc_pathologic_m == "
    		q9 += ajcc_pathologic_m[0]
    	else :
    		for i in ajcc_pathologic_m[:-1]:
    			q = "(ajcc_pathologic_m == "
    			q += i
    			q += " OR "
    			q9 += q
    		q = "ajcc_pathologic_m =="
    		q += ajcc_pathologic_m[-1]
    		q += ")"
    		q9 += q
    	l.append(q9)
    	
    if len(ajcc_pathologic_n) > 0 :
    	q10 = ""
    	if len(ajcc_pathologic_n) == 1 :
    		q10 = "ajcc_pathologic_n == "
    		q10 += ajcc_pathologic_n[0]
    	else :
    		for i in ajcc_pathologic_n[:-1]:
    			q = "(ajcc_pathologic_n == "
    			q += i
    			q += " OR "
    			q10 += q
    		q = "ajcc_pathologic_n =="
    		q += ajcc_pathologic_n[-1]
    		q += ")"
    		q10 += q
    	l.append(q10)
	
	if len(age_at_index) > 0 :
    	q11 = ""
    	if len(age_at_index) == 1 :
    		q11 = "age_at_index == "
    		q11 += age_at_index[0]
    	else :
    		for i in age_at_index[:-1]:
    			q = "(age_at_index == "
    			q += i
    			q += " OR "
    			q11 += q
    		q = "age_at_index =="
    		q += age_at_index[-1]
    		q += ")"
    		q11 += q
    	l.append(q11)
    
    if len(years_smoked) > 0 :
    	q12 = ""
    	if len(years_smoked) == 1 :
    		q12 = "years_smoked == "
    		q12 += years_smoked[0]
    	else :
    		for i in years_smoked[:-1]:
    			q = "(years_smoked == "
    			q += i
    			q += " OR "
    			q12 += q
    		q = "years_smoked =="
    		q += years_smoked[-1]
    		q += ")"
    		q12 += q
    	l.append(q12)

	if len(l) == 1:
		query += " WHERE "
		query += l[0]
	
	elif len(l) > 1:
		query += " WHERE "
		for i in l[:-1]:
			query += i
			query += " AND "
		query += l[-1]
	
	query1 += query	 	
	
	query2 += query
	
	try: cur.execute(query1)
	
	except pymysql.Error as e:
		print(e,query1)
		
	try: cur.execute(query2)
	
	except pymysql.Error as e:
		print(e,query2)

	results = cur.fetchall()
	
	print(json.dumps(results))
	
	conn.close()