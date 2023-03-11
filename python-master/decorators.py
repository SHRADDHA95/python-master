
import random
def highlighter(func):  
    annotations = ["!" ,"+", "*" , "%"]
    annotation = random.choice(annotations)

    def highlight(*name):
        print(annotation * 50)
        func(*name)
        print(annotation * 50)
    return highlight


def print_message(*name):
    print("message from print_message function" , name ,  end='\n')

def print_message02(*args):
    print("Just another method says Hi!")

hightlightandprint = highlighter(print_message)
hightlightandprint("shraddha")

hightlightandprint02 = highlighter(print_message02)
hightlightandprint02()

@highlighter
def print_message03(*args):
    print("Passed this fn through decorator annotation!" ,[arg.upper() for arg in args])

@highlighter
def print_message04(*args):
    print("Passed this fn through decorator annotation_002!" ,[arg.upper() for arg in args])

print_message03("pawan")
print_message04("shraddha")