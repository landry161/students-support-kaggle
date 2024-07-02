import pdb
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import duckdb

values=[]
def loadCSVFile():
    print("Création de notre nouveau fichier csv")
    arrayCSV=[]
    with open("Student_performance_data.csv",encoding="ISO-8859-1") as csvFile:
        myCSV=csv.reader(csvFile)
        header=next(myCSV)
        for row in myCSV:
            createNewFile(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])

#Création du fichier final  
def createNewFile(student_id,age,gender,ethnicity,parental_education,study_time_Weekly,absences,tutoring,parental_support,extracurricular,sports,music,volunteering,gpa,grade_class):
    fields=["student_id","age","gender","ethnicity","parental_education","study_time_Weekly","absences","tutoring","parental_support","extracurricular","sports","music","volunteering","gpa","grade_class"]
    values.append([student_id,age,returnGender(gender),returnEthnicity(ethnicity),parentalEducation(parental_education),study_time_Weekly,absences,returnTutoring(tutoring),parentalSupport(parental_support),returnExtraCurricular(extracurricular),sportParticipation(sports),musicParticipation(music),returnVolunteering(volunteering),gpa,gradeClass(grade_class)])
    #print(values)
    with open('final.csv', 'w', encoding='UTF8', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(fields)
        writer.writerows(values)

#Méthode qui retourne la liste des couleurs
def returnArrayColor(values):
    resultColors=[]
    colors=['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy','olive','purple','red','teal','white','yellow','silver','red','indigo','pink']
    for i in range(0,values):
        resultColors.append(colors[i])

    return resultColors

#Chart of parental Support
def chartParentalSupport():
    print("ok")
    mydf=pd.read_csv("final.csv",delimiter=",",encoding="UTF8")
    parentalSupport=duckdb.sql("SELECT parental_support, count(parental_support) as total FROM mydf GROUP BY parental_support").df()
    fig, ax = plt.subplots()

    parents=parentalSupport["parental_support"]
    y_pos = np.arange(len(parents))
    performance=parentalSupport["total"]
    error = np.random.rand(len(parents))

    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=parents)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Total')
    ax.set_title('The level of parental support')
    fig.show()
    plt.savefig("parentalSupport.png")

def chartParentParentalEducation():
    mydf=pd.read_csv("final.csv",delimiter=",",encoding="UTF8")
    parentalEducationLevel=duckdb.sql("SELECT parental_education,count(parental_education) as total FROM mydf GROUP BY parental_education").df()
    
    parentEducation=np.array(parentalEducationLevel["parental_education"])
    counterValues=np.array(parentalEducationLevel["total"])
    bar_labels =counterValues
    bar_colors =returnArrayColor(len(counterValues))
    fig, ax = plt.subplots()

    ax.bar(parentEducation,counterValues,label=bar_labels,color=bar_colors)
    ax.set_ylabel("Total")
    ax.set_title("The education level of the parents")
    ax.legend(title="Values")
    fig.show()
    plt.savefig("parentalEducation.png")
    
def showCharts():
    print("Affichage des graphes")
    mydf=pd.read_csv("final.csv",delimiter=",",encoding="ISO-8859-1")
    mysqldf=duckdb.sql("SELECT ethnicity,count(*) as total FROM mydf GROUP BY ethnicity").df()
    labels=mysqldf["ethnicity"]
    size=mysqldf["total"]
    fig,ax=plt.subplots()
    ax.pie(size,labels=labels,autopct='%1.1f%%')
    plt.legend(loc="upper left")
    plt.title("Proportion by Gender")
    fig.show()
    plt.savefig("pie_gender.png")

#gradeClass
def gradeClass(value):
    response=""
    print(value)
    if float(value)<2.0:
        response="F"
    elif float(value)>=2.0 and float(value)<2.5:
        response="D"
    elif float(value)>=2.5 and float(value)<3.0:
        response="C"
    elif float(value)>=3.0 and float(value)<3.5:
        response="B"
    else:
        response="A"
    return response

#Volontaire
def returnVolunteering(value):
    volunteeringResponse="Non" if int(value)==0 else "Oui"

    return volunteeringResponse

#MusicParticipation
def musicParticipation(musicValue):
    musicRespponse="Non" if int(musicValue)==0 else "Oui"

    return musicRespponse

#Sport participation
def sportParticipation(sportValue):
    sportResponse="Non" if int(sportValue)==0 else "Oui"

    return sportResponse


#Extracurricular
def returnExtraCurricular(value):
    response="Non" if int(value)==0 else "Oui"

    return response

#Tutoring Function
def returnTutoring(tutoringValue):
    response="Non" if int(tutoringValue)==0 else "Oui"

    return response

#Parental Support
def parentalSupport(parentalLevel):
    match int(parentalLevel):
        case 0:
            return "Aucun"
        case 1:
            return "Faible"
        case 2:
            return "Modéré"
        case 3:
            return "Elevé"
        case 4:
            return "Très élevé"

#Niveau d'étude des parents 
def parentalEducation(level):
    match int(level):
        case 0:
            return "Aucun"
        case 1:
            return "Lycée"
        case 2:
            return "Collège"
        case 3:
            return "Baccalauréat"
        case 4:
            return "Supérieur"

#Ethnicity Function
def returnEthnicity(ethnicityValue):
    response=""
    match int(ethnicityValue):
        case 0:
            return "Caucasian"
        case 1:
            return "African American"
        case 2:
            return "Asian"
        case 3:
            return "Other"


#Fonction du GENRE
def returnGender(value):
    gender="Male" if int(value)==0 else "Female"
    return gender

loadCSVFile()
chartParentalSupport()
showCharts()
chartParentParentalEducation()