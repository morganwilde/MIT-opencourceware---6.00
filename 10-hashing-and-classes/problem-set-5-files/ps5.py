# -*- coding: utf-8 -*-
# 6.00 Problem Set 5
# RSS Feed Filter

import sys
sys.dont_write_bytecode = True # stop generating *.pyc files

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid       = guid      # a string that serves as a unique name for this entry
        self.title      = title     # a string
        self.subject    = subject   # a string
        self.summary    = summary   # a string
        self.link       = link      # a string

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def is_word_in(self, text):
        """
        returns True if `word` is in `text`
        """
        lowerWord = self.word.lower()
        textToWords = text.lower().split()
        wordFound = False
        punctuation = string.punctuation + '’“”'
        for eachWord in textToWords:
            # check if word is fully in eachWord
            if lowerWord in eachWord:
                leftovers = eachWord.replace(lowerWord, '')
                if len(leftovers) == 0:
                    wordFound = True
                    break
                else:
                    charsBefore = eachWord[:eachWord.find(lowerWord)]
                    charsAfter = eachWord[eachWord.find(lowerWord) + len(lowerWord):]
                    if len(charsBefore) > 0:
                        proceedS = charsBefore[-1] in punctuation
                    else:
                        proceedS = True
                    if len(charsAfter) > 0:
                        proceedE = charsAfter[0] in punctuation
                    else:
                        proceedE = True
                    if proceedS and proceedE:
                        wordFound = True
                        break

        return wordFound

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_title())

# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_subject())
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_summary())

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)
        
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        if self.phrase in story.get_subject():
            return True
        elif self.phrase in story.get_title():
            return True
        elif self.phrase in story.get_summary():
            return True
        else:
            return False


#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel free to change this line!
    filteredStories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                if not story in filteredStories:
                    filteredStories.append(story)                
    return filteredStories

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    triggerList = []
    for line in lines:
        words = line.split()
        if words[0] == 'ADD':
            for var in words[1:]:
                triggerList.append(vars()[var])
        else:
            selectTrigger = ''
            selectWord = line[line.find(words[1]) + len(words[1]) + 1:]
            if words[1] == 'SUBJECT':
                selectTrigger = SubjectTrigger(selectWord)
            elif words[1] == 'TITLE':
                selectTrigger = TitleTrigger(selectWord)
            elif words[1] == 'SUMMARY':
                selectTrigger = SummaryTrigger(selectWord)
            elif words[1] == 'PHRASE':
                selectTrigger = PhraseTrigger(selectWord)
            elif words[1] == 'AND':
                # AndTrigger
                selectTrigger = AndTrigger(vars()[words[2]], vars()[words[3]])
            elif words[1] == 'OR':
                selectTrigger = OrTrigger(vars()[words[2]], vars()[words[3]])
            elif words[1] == 'NOT':
                selectTrigger = NotTrigger(vars()[words[2]])
                
            # finish up and assign object to the name
            vars()[words[0]] = selectTrigger

    return triggerList
    
import thread


def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    t7 = TitleTrigger("news")
    triggerlist = [t1, t4, t7]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()
