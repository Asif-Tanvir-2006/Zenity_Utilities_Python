import os
global filters
filters = "*"
global title
title = "Choose file(s)"
global multiple
multiple=""
def notification(txt):
    os.system("zenity --notification --text='" + txt + "'")
def choosefile(*arguments):
    for i in arguments:
        if i=="multiple=true":
            multiple=" --multiple"
        if "title" in i:
            i=i.replace("title=", "")
            title = i
        if "filters" in i:
            i=i.replace("filters=", "")
            i=i.replace(",'", ", '")
            i= i.replace("'", "")
            i=i.replace("\"", "")
            filters = i
    os.system('zenity --file-selection --file-filter="' + filters + '" ' +  '--title="' + title + '"' + multiple + ' --separator="sprt_sprt_sprt" >> file.txt')
    with open(r'file.txt', 'r') as file:
        data = file.read()
        data = data.replace("sprt_sprt_sprt", "\n")
        data = data.replace("\"", "")
    with open(r'file.txt', 'w') as file:
        file.write(data)
    file_file = open("file.txt")
    file_contents = file_file.read()
    # print(file_contents)
    file_file = open("file.txt")
    file_contents = file_file.read()
    contents_split = file_contents.splitlines()
    file_file.close()
   
    try:
        os.remove("file.txt")
    except:
        pass
    if len(contents_split)==1:
        for i in contents_split:
            return(i) 
    else:
        return(contents_split)
def choosedir(*arguments):
    for i in arguments:
        if i=="multiple=true":
            multiple=" --multiple"
        if "title" in i:
            i=i.replace("title=", "")
            title = i
    os.system("zenity  --file-selection --title='" + title + "'" " --directory" + multiple +  ' --separator="sprt_sprt_sprt"' + " >> file.txt")
    
    with open(r'file.txt', 'r') as file:
        data = file.read()
        data = data.replace("sprt_sprt_sprt", "\n")
        data = data.replace("\"", "")
    with open(r'file.txt', 'w') as file:
        file.write(data)
    file_file = open("file.txt")
    file_contents = file_file.read()
    file_file = open("file.txt")
    file_contents = file_file.read()
    contents_split = file_contents.splitlines()
    file_file.close()
    try:
        os.remove("file.txt")
    except:
        pass

    if len(contents_split)==1:
        for i in contents_split:
            return(i) 
    else:
        return(contents_split)




