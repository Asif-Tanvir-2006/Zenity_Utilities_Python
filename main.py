import zenity_utils as zu

####Choose multiple files and get their path####
print(zu.choosefile("multiple=true", "filters='*.appimage', '*.png', '*.jpeg'", "title=Choose file"))


####Choose single file and get its path####
##Don't pass the multiple argument###
print(zu.choosefile("filters='*.appimage', '*.png', '*.jpeg'", "title=Choose file"))

####Choose multiple directories####
print(zu.choosedir("multiple=true", "title=Choose Directories"))


####Choose a single directory####
print(zu.choosedir())

###Send a notification###
zu.notification("hello")

 