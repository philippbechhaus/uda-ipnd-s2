#   fill-in-the-blanks
#   by Philipp

quiz_blanks = ["___1___", "___2___","___3___","___4___"] #blank codes in sample texts

quiz1_answers = ["theory","GPS","navigation","Earth"] #answers for paragraph_1
quiz2_answers = ["satellite","speed","atomic","nanosecond"] #answers for paragraph_2
quiz3_answers = ["Differential","Kinematik","relative","dilation"] #answers for paragraph_3


paragraph_1 = '''People often ask me "What good is Relativity?" It is a commonplace to think of Relativity as an abstract
and highly arcane mathematical ___1___ that has no consequences for everyday life. This is in fact far from the truth. Consider
for a moment that when you are riding in a commercial airliner, the pilot and crew are navigating to your destination with
the aid of the Global Positioning System ( ___2___ ). Further, many luxury cars now come with built-in ___3___ systems that
include ___2___ receivers with digital maps, and you can purchase hand-held ___2___ navigation units that will give you your position
on the ___4___ (latitude, longitude, and altitude) to an accuracy of 5 to 10 meters that weigh only a few ounces and cost
around $100.'''

paragraph_2 = '''The nominal GPS configuration consists of a network of 24 ___1___ s in high orbits around the Earth, but up to
30 or so ___1___ s may be on station at any given time. Each ___1___ in the GPS constellation orbits at an altitude of about
20,000 km from the ground, and has an orbital ___2___ of about 14,000 km/hour (the orbital period is roughly 12 hours - contrary
to popular belief, GPS ___1___ s are not in geosynchronous or geostationary orbits). The ___1___ orbits are distributed so
that at least 4 ___1___ s are always visible from any point on the Earth at any given instant (with up to 12 visible at one
time). Each ___1___ carries with it an ___3___ clock that "ticks" with an accuracy of 1 ___4___ (1 billionth of a second).
A GPS receiver in an airplane determines its current position and course by comparing the time signals it receives from a
number of the GPS ___1___ s (usually 6 to 12) and trilaterating on the known positions of each ___1___ . The precision
achieved is remarkable: even a simple hand-held GPS receiver can determine your absolute position on the surface of the Earth
to within 5 to 10 meters in only a few seconds. A GPS receiver in a car can give accurate readings of position, ___2___ , and
course in real-time!'''

paragraph_3 = '''More sophisticated techniques, like ___1___ GPS (DGPS) and Real-Time ___2___ (RTK) methods, can deliver
centimeter-level positions with a few minutes of measurement. Such methods allow GPS and related satellite navigation system data to
be used in precision surveying, autodrive systems, and other applications requiring greater position accuracy than achieved with
standard GPS receivers.To achieve this level of precision, the clock ticks from the GPS satellites must be known to an accuracy
of 20-30 nanoseconds. However, because the satellites are constantly moving ___3___ to observers on the Earth, effects predicted
by the Special and General theories of Relativity must be taken into account to achieve the desired 20-30 nanosecond accuracy. Because
an observer on the ground sees the satellites in motion ___3___ to them, Special Relativity predicts that we should see their clocks
ticking more slowly (see the Special Relativity lecture). Special Relativity predicts that the on-board atomic clocks on the satellites
should fall behind clocks on the ground by about 7 microseconds per day because of the slower ticking rate due to the time ___4___
effect of their ___3___ motion.'''

# ---prompt---
# Behavior: prompt examines if word is in the list quiz_blanks. If not, function returns None
# Input: word can be any String; quiz_blanks are pre-defined and are references inside paragraph_1,2,3
# Output: either word if String is found in quiz_blanks or None if word is not inside quiz_blanks

def prompt(word,quiz_blanks):    
    for blank in quiz_blanks:
        if blank in word:
            return blank
    return None


# ---change_blank---
# Behavior: change_blank switches all "blanks" in question with the respective "word" inside a "paragraph"
# Input: word can be any String, blank can be any String, paragraph can be any String containing >1 words
# Output: returns a new list of strings where "word" replaced "blank" 

def change_blank(word, blank, paragraph):
    count = 0
    newparagraph = paragraph
    while count < len(newparagraph):
        if newparagraph[count] in blank:
            newparagraph[count] = word
            count = count+1
        else:
            count = count+1
    return newparagraph


# ---initiation---    
# Behavior: initiation sets difficulty of quiz
# Input: None
# Output: String refering to level of experience

def initiation():
    beginnerlevel = 1
    advancedlevel = 2
    expertlevel = 3
    print "How do GPS satellites work?" "\n" "Quiz by Philipp Bechhaus" "\n" "\n"
    while True:
        try:
            experience = int(raw_input("How experienced are you?: " "\n" "\n" "Select" "\n" "1 for BEGINNER"
                           "\n" "2 for ADVANCED" "\n" "3 for PRO" "\n" "\n"))
        except ValueError:
            print "That's not a number!"
        else:
            if beginnerlevel <= experience <= expertlevel:
                break
            else:
                print "We're not there yet.."
    return experience


# ---setting functions---
# Behavior: set_paragraph, set_answerset and goodluck returns a pre-defined set of pararaphs, answers and goodluck sentences based on the level of experience
# Input: Integer 1 <= x <= 3
# Output: paragraph, list of quiz answers, good luck sentences

def set_paragraph(experience):
    if experience == 1:
        return paragraph_1
    if experience == 2:
        return paragraph_2
    if experience == 3:
        return paragraph_3

def set_answerset(experience):
    if experience == 1:
        return quiz1_answers
    if experience == 2:
        return quiz2_answers
    if experience == 3:
        return quiz3_answers

def goodluck(experience):
    if experience == 1:
        return "You've selected BEGINNER. Let's get started!" "\n" "You have 4 lifelines. Be careful!" "\n"
    if experience == 2:
        return "You've selected ADVANCED. Be prepared!" "\n" "You have 4 lifelines. Be careful!" "\n"
    if experience == 3:
        return "You've selected PRO. Good luck!" "\n" "You have 4 lifelines. Be careful!" "\n"


# ---nextLevel---
# Behavior: prints the (updated) joined solution paragraph
# Input: old solution list
# Output: new solution paragraph

def joinSolution(solution):
    print "\n" 
    return " ".join(solution) + "\n" + "\n"


# ---answerCheck---
# Behavior: checks if the given answer is equal to pos in list of answer_set. If it is, function returns "true", else "false"
# Input: replacement-String (must be a quiz_blank), selected list of answers, pos in list, old solution list
# Output: String true or String false

def answerCheck(replacement,answer_set,pos,solution):
        try:
            user_input = str(raw_input("Please insert your answer for " + replacement + ": "))
        except ValueError:
            print "We are looking for words!"
        else:
            if user_input == answer_set[pos]:
                solution = change_blank(user_input,replacement,solution)
                print "\n" "Good! Correct answer!" "\n" "-"
                return "true"
            else:
                print "\n" "Incorrect, try again!"
                return "false"


# ---game_process---
# Behavior: loops through the solution list, finds quiz_blanks, prompts the quiz and modifies the solution list accordingly once answer is correct and counter is >0
# Input: pre-defined quiz_blanks, selected paragraph and selected list of answers
# Output: solution paragraph to quiz or String "Game over" once lifelines are exceeded

def game_process(quiz_blanks,paragraph,answer_set):
    counter = 4
    pos = 0
    solution = paragraph.split()
    for word in solution:
        replacement = prompt(word,quiz_blanks)
        if counter != 0:
            if replacement != None:
                print joinSolution(solution)
                while counter != 0:
                    answer = answerCheck(replacement,answer_set,pos,solution)
                    if answer == "false":
                        counter = counter - 1
                        print "You have " + str(counter) + " more lifelines!" "\n"
                    else:
                        pos = pos + 1
                        break
        else:
            return "\n" ":( Game over!"
    solution = " ".join(solution)
    print "\n" "\n" "Awesomesauce! You've done it!" "\n"
    return solution


# ---
# play is the umbrella function for running a normal game combining functions above

def play(quiz_blanks):
    experience = initiation()
    paragraph = set_paragraph(experience)
    answer_set = set_answerset(experience)
    print goodluck(experience)
    return game_process(quiz_blanks,paragraph,answer_set)


# ---
# run game 

print play(quiz_blanks)


        
