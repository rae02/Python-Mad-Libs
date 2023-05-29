'''
Created on Feb. 5, 2023

@author: raeed
'''
import random

def choosestory():
    """Chooses 1 story template from a list of templates"""
    
    global story1,stories,story2,story3
    
    
    
    story1 = 'This weekend I am going camping with {}.\nI packed my lantern, sleeping bag, and {}.\nI am so {} to {} in a tent.\nI am {} we might see a {}, they are kind of dangerous.\nWe are going to hike, fish, and {}.\nI have heard that the {} lake is great for {}.\nThen we will {} hike through the forest for {} {}.\nIf I see a {} {} while hiking, I am going to bring it home as a pet!\nAt night we will tell {} {} stories and roast {} around the campfire!'
    story2 = "It was about {} {} ago when I came to the hospital in a {}.\n The hospital is a/an {} place, there are a lot of {} {} here.\n There are nurses who have {} {}. \n If someone wants to come into my room I told them that they have to {} first.\n I have decorated my room with {}.\n Today a doctor came into my room and they were wearing a {} on their {}.\n I heard that all doctors {} {} every day for breakfast.\n The most {} thing about being in the hospital is the {} {}." 
    story3 = 'Dear {}\nIam writing to you from {} castle in an enhanced forest.\nI found myself here one day after going for a ride on a {} {} in {}. There are {} {} and {} {} here!\n In the {} there is a pool full of {}. \nI fall asleep each night on a {} of {} and dream of {} {}. \nIt feels as though I have lived here for {} {}.\nI hope one day you can visit, although the only way to get here now is {} on a {} {}!!'
    stories = [story1, story2, story3]
    
    i =random.randint(0,len(stories)-1)
    
    chosen = stories[i]
    
    return chosen


def create():
    global final
    
    chosen = choosestory()
    if chosen == story1:
        a1 = input("Person's name: ")
        a2 = input('Noun: ')
        a3 = input("Feeling Adjective: ")
        a4 = input("Verb: ")
        a5 = input('Feeling Adjective: ')
        a6 = input('Animal: ')
        a7 = input('Verb: ')
        a8 = input('Colour: ')
        a9 = input('Verb (ending in "ing": ')
        a10 = input('Adverb (ending in "ly"): ')
        a11 = input('Number: ')
        a12 = input('Measure of time: ')
        a13 = input('Colour: ')
        a14 = input('Animal: ')
        a15 = input('Number: ')
        a16 = input('Silly Word: ')
        a17 = input('Noun: ')
        print()
        print()
        
        final = (chosen.format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17))
    elif chosen == story2:
        a1 = input('Number: ')
        a2 = input('Measure of time: ')
        a3= input('Mode of transportation: ')
        a4 = input('Adjective: ')
        a5 = input('Adjective: ')
        a6 = input('Noun: ')
        a7 = input('Colour: ')
        a8 = input('Part of the body: ')
        a9 = input('Verb: ')
        a10 = input('Number: ')
        a11 = input('Noun: ')
        a12 = input('Noun: ')
        a13 = input('Part of the body: ')
        a14 = input('Verb: ')
        a15 = input('Noun: ')
        a16 = input('Adjective: ')
        a17 = input('Silly word: ')
        a18 = input('Noun: ')
        print()
        print()
        
        final = chosen.format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18)
    elif chosen == story3:
        a1 = input("Person's name: ")
        a2 = input('Adjective: ')
        a3 = input('Colour: ')
        a4 = input('Animal: ')
        a5 = input('Place: ')
        a6 = input('Adjective: ')
        a7 = input('Magical Creature (Plural): ')
        a8 = input('Adjective: ')
        a9 = input('Magical Creature: ')
        a10 = input('Room in house: ')
        a11 = input('Noun: ')
        a12 = input('Noun: ')
        a13 = input('Noun: ')
        a14 = input('Adjective: ')
        a15 = input('Noun (plural): ')
        a16 = input('Number: ')
        a17 = input('Measure of time: ')
        a18 = input('Verb (ending in "ing"): ')
        a19 = input('Adjective: ')
        a20 = input('Noun: ')
        print()
        print()
        final = chosen.format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20)
    
    
    return final 

def elite():
    
    print()
    feedback = input('Does this make it to the elite list? (Y/N): ')
    feedback = feedback.upper()
    if feedback == 'Y': 
        file = open('elite.txt',"a")
        file.write("\n\n {}".format(final))
    return

def madlib():
    
    print(create())
    elite()
    
    
    return
