### ΕΙΣΑΓΩΓΗ ΔΙΑΦΟΡΩΝ MODULE
import tkinter
import tkinter.ttk
from tkinter import filedialog
import sys
from sys import *
import openpyxl
import numpy as np
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

###########################ΜΕΤΑΒΛΗΤΕΣ ΠΡΟΓΡΑΜΜΑΤΟΣ####################################################
WILDCARD = 2 # ΔΗΛΩΝΕΙ ΠΟΣΑ ΜΑΤΣ ΠΡΕΠΕΙ ΝΑ ΠΑΙΞΕΙ Ο ΠΑΙΧΤΗΣ ΓΙΑ ΝΑ ΠΑΡΕΙ ΜΠΑΛΑΝΤΕΡ           
MAX_CHALLENGES_OUT = 1 # ΔΗΛΩΝΕΙ ΠΟΣΕΣ ΠΡΟΚΛΗΣΕΙΣ ΜΠΟΡΕΙ ΝΑ ΣΤΕΙΛΕΙ ΕΝΑΣ ΠΑΙΚΤΗΣ           
MAX_CHALLENGES_IN = 1 # ΔΗΛΩΝΕΙ ΠΟΣΕΣ ΠΡΟΚΛΗΣΕΙς ΜΠΟΡΕΙ ΝΑ ΔΕΧΤΕΙ ΕΝΑΣ ΠΑΙΚΤΗΣ
MAX_ACTIVE_CHALLENGES = 1 # ΔΗΛΩΝΕΙ ΤΟΝ ΜΕΓΙΣΤΟ ΑΡΙΘΜΟ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΜΠΟΡΕΙ ΝΑ ΑΠΟΔΕΚΤΕΙ ΕΝΑΣ ΠΑΙΧΤΗΣ
MAX_RANKING_CHALLENGE = 3 # ΔΗΛΩΝΕΙ ΤΗΝ ΜΕΓΙΣΤΗ ΑΠΟΣΤΑΣΗ(ΔΙΑΦΟΡΑ ΚΑΤΑΤΑΞΗΣ) ΠΟΥ ΠΡΕΠΕΙ ΝΑ ΕΧΟΥΝΕ ΟΙ ΠΑΙΚΤΕΣ ΓΙΑ ΝΑ ΣΤΕΙΛΟΥΝΕ ΠΡΟΚΛΗΣΗ
POINT_SET_MATCH =3 # ΟΡΙΖΕΙ ΤΟΝ ΜΕΓΙΣΤΟ ΑΡΙΘΜΟ ΣΕΤ ΠΟΥ ΠΡΕΠΕΙ ΝΑ ΠΑΡΕΙ ΕΝΑΣ ΠΑΙΚΤΗΣ ΓΙΑ ΝΑ ΚΕΡΔΙΣΕΙ ΤΟ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ
global filename_player_data # ΔΗΛΩΝΕΙ ΤΟ ΑΡΧΕΙΟ ΕXCEL ΠΟΥ ΣΩΖΟΝΤΑΙ ΤΑ ΣΤΟΙΧΕΙΑ ΤΩΝ ΠΑΙΚΤΩΝ
global filename_out_ch # ΔΗΛΩΝΕΙ ΤΟ ΑΡΧΕΙΟ ΤΩΝ ΕΚΡΕΜΩΝ ΠΡΟΚΛΗΣΕΩΝ ΤΩΝ ΠΑΙΚΤΩΝ
global filename_valid_ch  # ΔΗΛΩΝΕΙ ΤΟ ΑΡΧΕΙΟ ΤΩΝ ΑΠΟΔΕΚΤΩΝ(ΕΝΕΡΓΩΝ) ΠΡΟΚΛΗΣΕΩΝ ΤΩΝ ΠΑΙΚΤΩΝ
################################################################################################

######################################################
###EXCEL  ΕΠΙΚΕΦΑΛΙΔΕΣ                             ##
######################################################
heads_ch_valid_match = ['giver_name','giver_surname','giver_serial','taker_name','taker_surname','taker_serial']##ΕΠΙΚΕΦΑΛΙΔΕΣ ΓΙΑ ΤΑ ΕΓΚΥΡΑ ΜΑΤΣ ΠΡΟΚΛΗΣΕΩΝ
heads_ch_out_match = ['giver_name','giver_surname','giver_serial','taker_name','taker_surname','taker_serial']##ΕΠΙΚΕΦΑΛΙΔΕΣ ΓΙΑ ΤΑ ΜΗ ΕΓΚΥΡΑ ΜΑΤΣ ΠΡΟΚΛΗΣΕΩΝ
heads_players = ['name','surname','age','matches_played','matches_won','matches_lost','sets_won','sets_lost','wildcard_state','challenges_given_state','challenges_taken_state','challenges_given','challenges_taken','challenges_final','challenges_final_state']#ΛΙΣΤΑ ΜΕ ΕΠΙΚΕΦΑΛΙΔΕΣ ΓΙA ΤΟΥΣ ΠΑΙΧΤΕΣ
######ΛΙΣΤΕΣ ##########################################
#######################################################
player_data = []    # ΛΙΣΤΑ ΑΠΟΘΗΚΕΥΣΗΣ ΤΩΝ ΣΤΟΙΧΕΙΩΝ player_data_main

player_data_main = [] # ΑΠΟΘΗΚΕΥΕΙ ΤΙΣ ΚΛΑΣΕΙΣ ΠΑΙΚΤΗ

ch_out_matches = [] #ΛΙΣΤΑ ΑΠΟΘΗΚΕΥΣΗΣ ΤΩΝ ΣΤΟΙΧΕΙΩΝ ch_out_matches_main

ch_out_matches_main = [] #ΑΠΟΘΗΚΕΥΕΙ ΤΙΣ ΚΛΑΣΕΙΣ ΤΩΝ ΜΑΤΣ ΠΡΟΣ ΑΠΟΔΟΧΗ Η ΑΠΟΡΡΙΨΗ

ch_valid_matches = [] #ΛΙΣΤΑ ΑΠΟΘΗΚΕΥΣΗΣ ΤΩΝ ΣΤΟΙΧΕΙΩΝ ch_valid_matches

ch_valid_matches_main = [] #ΑΠΟΘΗΚΕΥΕΙ ΤΙΣ ΚΛΑΣΕΙΣ ΤΩΝ ΜΑΤΣ ΠΟΥ ΕΓΙΝΑΝ ΑΠΟΔΕΚΤΑ

##################################################################################
#ΕΓΡΑΦΗ ΚΑΙ ΑΝΑΓΝΩΣΗ ΔΕΔΟΜΕΝΩΝ ΣΕ ΑΡΧΕΙΑ
##################################################################################
    
def open_excel_file(filename,data): ##  ΑΝΟΙΓΕΙΕ ΕΝΑ ΑΡΧΕΙΟ EXCEL.XLSL ΚΑΙ ΑΝΤΙΓΡΑΦΕΙ ΤΑ ΠΕΡΙΕΧΟΜΕΝΑ ΤΟΥ ΣΕ ΜΙΑ ΛΙΣΤΑ
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    max_row = sheet.max_row
    max_col = sheet.max_column
    for i in range(2, max_row+1):
        for j in range( 1, max_col+1):
            cell = sheet.cell(i,j)
            data.append(cell.value) 
    return 
    
def write_excel_file(filename,data,heads): ## ΑΝΤΙΓΡΑΦΕΙ ΤΑ ΔΕΔΟΜΕΝΑ ΜΙΑΣ ΛΙΣΤΑ ΣΕ ΕΝΑ ΦΥΛΛΟ EXCEL.XLSL ΕΙΣΟΔΟΙ -- ΟΝΟΜΑ ΑΡΧΕΙΟΥ--ΛΙΣΤΑ ΜΕ ΤΑ ΣΤΟΙΧΕΙΑ ΤΩΝ ΠΑΙΧΤΩΝ--ΛΙΣΤΑ ΜΕ ΚΕΦΑΛΙΔΕΣ ΓΙΑ ΤΟ ΕXCEL   
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    temp = matrix(data,heads)
    
    for i in range(len(heads)):
        cell = sheet.cell(1,i+1)
        cell.value = heads[i]
        
        
    for row in range(len(temp)):
        for column in range(len(temp[row])):
            cell = sheet.cell(row+2,column+1)
            cell.value=temp[row][column]
            
    wb.save(filename)
    return   

def matrix(list_a,list_b):  #ΜΕΤΑΤΡΕΠΕΙ ΠΙΝΑΚΑ ΜΙΑΣ ΔΙΑΣΤΑΣΗΣ ΣΕ ΠΙΝΑΚΑ ΔΥΟ ΔΙΑΣΤΑΣΕΩΝ ΜΕ ΤΟ NUMPY
    temp = np.array(list_a)
    new_temp=np.reshape(temp,(int(len(list_a)/len(list_b)),len(list_b)))
    return new_temp
    
    
  
#####################################################################
#############ΚΛΑΣΗ ΠΑΙΚΤΗ ###########################################
#####################################################################
class Player:
    def __init__(self,name,surname,age,matches_played,matches_won,matches_lost,sets_won,sets_lost,wildcard_state,challenges_given_state,challenges_taken_state,challenges_given,challenges_taken,challenges_final,challenges_final_state):
        self.name = name # ΟΝΟΜΑ
        self.surname = surname #ΕΠΩΝΥΜΟ
        self.age = age # ΗΛΙΚΙΑ
        self.matches_won = matches_won # ΚΕΡΔΙΣΜΕΝΑ ΠΑΙΧΝΙΔΙΑ
        self.matches_lost = matches_lost #ΧΑΜΕΝΑ ΠΑΙΧΝΙΔΙΑ
        self.matches_played = matches_played # ΣΥΝΟΛΟ ΠΑΙΧΝΙΔΙΩΝ
        self.sets_won = sets_won # SETS ΠΟΥ ΚΕΡΔΙΣΕ Ο ΠΑΙΚΤΗΣ
        self.set_lost = sets_lost # SETS ΠΟΥ ΕΧΑΣΕ Ο ΠΑΙΚΤΗΣ
        self.wildcard_state = wildcard_state # WILDCARD STATE FALSE(0) TRUE(1) ΚΑΤΑΣΤΑΣΗ ΤΟΥ ΜΠΑΛΑΝΤΕΡ
        self.challenges_given_state = challenges_given_state # ΚΑΤΑΣΤΑΣΗ ΤΟΥ ΑΝ ΜΠΟΡΕΙ ΝΑ ΔΩΣΕΙ ΠΡΟΚΛΗΣΕΙΣ FALSE(0) OR TRUE(1) 
        self.challenges_taken_state = challenges_taken_state # ΚΑΤΑΣΤΑΣΗ ΤΟΥ ΑΝ ΜΠΟΡΕΙ ΝΑ ΔΕΚΤΕΙ ΠΡΟΚΛΗΣΗ FALSE(0) OR TRUE(1)
        self.challenges_given = challenges_given # ΑΡΙΘΜΟΣ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΕΧΕΙ ΔΩΣΕΙ Ο ΠΑΙΚΤΗΣ ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΕΙΝΑΙ ΜΕΓΑΛΥΤΕΡΟ ΑΠΟ ΤΟ MAX_CHALLENGES_OUT
        self.challenges_taken = challenges_taken # ΑΡΙΘΜΟΣ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΜΠΟΡΕΙ ΝΑ ΔΕΚΤΕΙ Ο ΠΑΙΚΤΗΣ ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΕΙΝΑΙ ΜΕΓΑΛΥΤΕΡΟ ΑΠΟ ΤΟ MAX_CHALLENGES_IΝ
        self.challenges_final = challenges_final # ΑΡΙΘΜΟΣ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΕΧΕΙ ΑΠΟΔΕΚΤΕΙ Ο ΠΑΙΚΤΗΣ ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΕΙΝΑΙ ΜΕΓΑΛΥΤΕΡΟ ΑΠΟ ΤΟ MAX_ACTIVE_CHALLENGES
        self.challenges_final_state = challenges_final_state # ΚΑΤΑΣΤΑΣΗ ΤΟΥ ΕΑΝ Ο ΠΑΙΚΤΗΣ ΜΠΟΡΕΙ ΝΑ ΑΠΟΔΕΚΤΕΙ ΑΛΛΕΣ ΠΡΟΚΛΗΣΕΙΣ FALSE(0) OR TRUE(1)
    
        
    def increase_challenges_final(self): ###ΑΥΞΑΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΤΟΝ ΑΠΟΔΕΚΤΩΝ ΠΡΟΚΛΗΣΕΩΝ
        self.challenges_final +=1
        return self.challenges_final
    
    def decrease_challenges_final(self): ## ΜΕΙΩΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΑΠΟΔΕΚΤΩΝ ΠΡΟΚΛΗΣΕΩΝ
        self.challenges_final -=1
        return self.challenges_final

    def decrease_challenges_given(self): ##ΜΕΙΩΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΕΔΩΣΕ Ο ΠΑΙΚΤΗΣ
        self.challenges_given -=1
        return self.challenges_given
    
    def decrease_challenges_taken(self): ##ΜΕΙΩΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΔΕΧΤΗΚΕ Ο ΠΑΙΚΤΗΣ
        self.challenges_taken -=1
        return self.challenges_taken

    def alter_challenges_final_state(self): # ΕΛΕΓΧΕΙ  ΤΟ ΕΑΝ Ο ΠΑΙΚΤΗΣ ΕΧΕΙ ΑΠΟΔΕΚΤΕΙ ΠΕΡΙΣΣΟΤΕΡΕΣ ΠΡΟΚΛΗΣΕΙΣ ΑΠΟ ΤΙΣ ΕΠΙΤΡΕΠΟΜΕΝΕΣ
        if(self.challenges_final>=MAX_ACTIVE_CHALLENGES):
            self.challenges_final_state=0
        else: self.challenges_final_state = 1
        return self.challenges_final_state
        
    def reset_challenges_final(self): ### ΕΠΑΝΑΦΕΡΕΙ ΤΟΝ ΑΡΙΘΜΟ ΤΟΝ ΕΝΕΡΓΩΝ ΠΡΟΚΛΗΣΕΩΝ ΣΕ ΚΑΤΑΣΤΑΣΗ TRUE(1)
        self.challenges_final = 1
        return self.challenges_final

    def increase_challenges_given(self):##ΑΥΞΑΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΕΔΩΣΕ Ο ΠΑΙΚΤΗΣ
        self.challenges_given +=1
        return self.challenges_given
    
    def increase_challenges_taken(self): ## ΑΥΞΑΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΔΕΚΤΗΚΕ Ο ΠΑΙΚΤΗΣ
        self.challenges_taken +=1
        return self.challenges_taken
        
    def reset_challenges_given(self): ## ΕΠΑΝΑΦΕΡΕΙ ΤON AΡΙΘΜΟ ΤΩΝ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΕΔΩΣΕ Ο ΠΑΙΚΤΗΣ ΣΕ (0)
        self.challenges_given =0
        return self.challenges_given
    
    def reset_challenges_taken(self): ## ΕΠΑΝΑΦΕΡΙ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΠΡΟΚΛΗΣΕΩΝ ΠΟΥ ΔΕΧΤΗΚΕ Ο ΠΑΙΚΤΗΣ ΣΕ (0)
        self.challenges_taken = 0
        return self.challenges_taken
    
    def increase_matches_won(self):# ΑΥΞΑΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΜΑΤΣ ΠΟΥ ΚΕΡΔΙΣΕ Ο ΠΑΙΚΤΗΣ
        self.matches_won+=1
        return self.matches_won
    
    def increase_matches_played(self):# ΑΥΞΑΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΜΑΤΣ ΠΟΥ ΕΠΑΙΞΕ Ο ΠΑΙΚΤΗΣ
        self.matches_played +=1
        return self.matches_played
    
    def increase_matches_lost(self):# ΑΥΞΑΝΕΙ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΜΑΤΣ ΠΟΥ ΕΧΑΣΕ Ο ΠΑΙΚΤΗΣ
        self.matches_lost+=1
        return self.matches_lost
        
    def increase_sets_won(self,number): # ΑΥΞΑΝΕΙ ΚΑΤΑ ΑΡΙΘΜΟ ΕΙΣΟΔΟΥ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΣΕΤΣ ΠΟΥ ΕΧΕΙ ΚΕΡΔΙΣΕΙ Ο ΠΑΙΚΤΗΣ
        self.sets_won += number
        return self.sets_won
        
    def increase_sets_lost(self,number):# ΑΥΞΑΝΕΙ ΚΑΤΑ ΑΡΙΘΜΟ ΕΙΣΟΔΟΥ ΤΟΝ ΑΡΙΘΜΟ ΤΩΝ ΣΕΤΣ ΠΟΥ ΕΧΕΙ ΧΑΣΕΙ Ο ΠΑΙΚΤΗΣ
        self.set_lost += number
        return self.set_lost
    
    def reset_wildcard_state(self):# ΕΛΕΓΧΕΙ ΑΝ ΕΧΕΙ ΠΑΙΞΕΙ Ο ΠΑΙΚΤΗΣ ΠΑΙΧΝΙΔΙΑ ΟΣΑ ΠΡΕΠΕΙ ΓΙΑ ΝΑ ΠΑΡΕΙ ΜΠΑΛΑΝΤΕΡ
        if(self.matches_played>0 and self.matches_played%WILDCARD==0):
            self.wildcard_state == 1
        return

    def alter_wildcard_state(self): # ΑΛΛΑΖΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΤΟΥ ΜΠΑΛΑΝΤΕΡ ΕΑΝ Ο ΠΑΙΚΤΗΣ ΕΧΕΙ ΠΑΙΞΕΙ ΠΑΡΑΠΑΝΩ ΠΑΙΧΝΙΔΙΑ ΑΠΟ ΤΑ ΕΠΙΤΡΕΠΟΜΕΝΑ ΑΛΛΙΩΣ ΤΗΝ ΑΦΗΝΕΙ ΩΣ ΕΧΕΙ
        if(self.matches_played>=WILDCARD):
            self.wildcard_state=1
        else:
            self.wildcard_state=0
        return self.wildcard_state

    def alter_challenges_given_state(self): # ΕΛΕΧΕΙ ΕΑΝ Ο ΠΑΙΚΤΗΣ ΕΧΕΙ ΔΩΣΕΙ ΠΑΡΑΠΑΝΩ ΠΡΟΚΛΗΣΕΙΣ ΑΠΟ ΤΙΣ ΕΠΙΤΡΕΠΤΕΣ ΚΑΙ ΑΛΛΑΖΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΤΗΣ ΑΝΑΛΟΓΗΣ ΜΕΤΑΒΛΗΤΗΣ
        if(self.challenges_given>=MAX_CHALLENGES_OUT):
            self.challenges_given_state=0
        else: self.challenges_given_state=1
        return self.challenges_given_state
    
    def alter_challenges_taken_state(self): # ΕΛΕΓΧΕΙ ΕΑΝ Ο ΠΑΙΚΤΗΣ ΕΧΕΙ ΔΕΚΤΕΙ ΠΑΡΑΠΑΝΩ ΠΡΟΚΛΗΣΕΙΣ ΑΠΟ ΤΙΣ ΕΠΙΤΡΕΠΤΕΣ ΚΑΙ ΑΛΛΑΖΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΤΗΣ ΑΝΑΛΟΓΗΣ ΜΕΤΑΒΛΗΤΗΣ
        if(self.challenges_taken>=MAX_CHALLENGES_IN):
            self.challenges_taken_state=0
        else:
            self.challenges_taken_state=1
        return self.challenges_taken_state
    
    def __str__(self): # ΤΥΠΩΝΕΙ ΤΗΝ ΚΛΑΣΗ ΠΑΙΧΤΗ ΓΙΑ ΤΗΝ ΕΚΤΥΠΩΣΗ ΒΑΣΙΚΗΣ ΚΑΤΑΤΑΞΗΣ
        return f"Ονομα\t\t{self.name}\t\tΕπώνυμο\t\t{self.surname}\t\tΗλικία\t\t{self.age}"
    
    def __str__stats__(self):# ΤΥΠΩΝΕΙ ΤΗΝ ΚΛΑΣΗ ΠΑΙΚΤΗ ΓΙΑ ΤΗΝ ΕΚΤΥΠΩΣΕΗ ΚΑΤΑΤΑΞΗΣ ΜΕ ΣΤΑΤΙΣΤΙΚΑ
        return f"{self.name}\t\t{self.surname}\t\tΣύνολο\t{self.matches_played}\tΝίκες\t{self.matches_won}\tΗττες\t{self.matches_lost}\tΚερδισμένα σετ\t{self.sets_won}\tΧαμένα σετ\t{self.set_lost}"

###############################################################
#### CLASS CHALLENGE MATCH                                  ###
###############################################################

class Challenge_Match:
    def __init__(self,giver_name,giver_surname,giver_serial,taker_name,taker_surname,taker_serial):
        self.name_giver = giver_name  # ΟΝΟΜΑ ΠΑΙΚΤΗ ΠΟΥ ΔΙΝΕΙ ΤΗΝ ΠΡΟΚΛΗΣΗ
        self.name_taker = taker_name  # ΟΝΟΜΑ ΠΑΙΚΤΗ ΠΟΥ ΕΙΝΑΙ ΣΤΟΧΟΣ ΤΗΣ ΠΡΟΚΛΗΣΗΣ
        self.giver_surname = giver_surname    #ΕΠΩΝΥΜΟ ΠΑΙΚΤΗ ΠΟΥ ΔΙΝΕΙ ΤΗΝ ΠΡΟΚΛΗΣΗ
        self.taker_surname = taker_surname   # ΕΠΩΝΥΜΟ ΠΑΙΚΤΗ ΠΟΥ ΕΙΝΑΙ ΣΤΟΧΟΣ ΤΗΣ ΠΡΟΚΛΗΣΗΣ
        self.taker_serial = taker_serial #ΑΡΙΘΜΟΣ ΚΑΤΑΤΑΞΗΣ ΠΑΙΚΤΗ ΠΟΥ ΕΙΝΑΙ ΣΤΟΧΟΣ ΤΗΣ ΠΡΟΚΛΗΣΗΣ
        self.giver_serial = giver_serial # ΑΡΙΘΜΟΣ ΚΑΤΑΤΑΞΗΣ ΠΑΙΚΤΗ ΠΟΥ ΔΙΝΕΙ ΤΙΝ ΠΡΟΚΛΗΣΗ

    def __str__(self): ## ΕΚΤΥΠΩΣΗ ΤΗΣ ΚΛΑΣΗΣ ΓΙΑ ΤΑ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ
        return f"Κατάταξη\t{self.taker_serial+1}\t{self.name_taker}\t{self.taker_surname}\t\tVS\t\tΚατάταξη\t{self.giver_serial+1}\t{self.name_giver}\t{self.giver_surname}"

################################################################        
####ΓΡΑΦΕΙ ΣΤΗΝ PLAYER_DATA_MAIN                  ##############
################################################################      
def create_player_classes(name,surname,age): # ΑΥΤΗ Η ΣΥΝΑΡΤΗΣΗ ΔΗΜΙΟΥΡΓΕΙ ΜΙΑ ΝΕΑ ΚΛΑΣΗ ΠΑΙΚΤΗ ΚΑΙ ΤΗΝ ΤΟΠΟΘΕΤΕΙ ΣΤΟ ΤΕΛΟΣ ΤΗΣ ΛΙΣΤΑΣ PLAYER_DATA_MAIN
    player_data_main.append(Player(name,surname,age,matches_played=0,matches_won=0,matches_lost=0,sets_won=0,sets_lost=0,wildcard_state=1,challenges_given_state=0,challenges_taken_state=0,challenges_given=0,challenges_taken=0,challenges_final=0,challenges_final_state=1))
    return

def load_class_player(filename,list): #ΑΥΤΗ Η ΣΥΝΑΡΤΗΣΗ ΦΟΡΤΩΝΕΙ ΤΑ ΣΤΟΙΧΕΙΑ ΤΗΣ ΚΛΑΣΗΣ ΠΑΙΚΤΗ ΑΠΟ ΤΟ ΦΥΛΛΟ EXCEL ΚΑΝΟΝΤΑΣ ΧΡΗΣΗ ΤΗΣ ΟPENPYXL
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    max_row = sheet.max_row
    for i in range(2, max_row+1):
        cellA = sheet.cell(i,1)
        cellB = sheet.cell(i,2)
        cellC = sheet.cell(i,3)
        cellD = sheet.cell(i,4)
        cellE = sheet.cell(i,5)
        cellF = sheet.cell(i,6)
        cellG = sheet.cell(i,7)
        cellH = sheet.cell(i,8)
        cellI = sheet.cell(i,9)
        cellJ = sheet.cell(i,10)
        cellK = sheet.cell(i,11)
        cellL = sheet.cell(i,12)
        cellM = sheet.cell(i,13)
        cellN = sheet.cell(i,14)
        cellO = sheet.cell(i,15)
        name=cellA.value
        surname=cellB.value
        age=int(cellC.value)
        matches_played=int(cellD.value)
        matches_won=int(cellE.value)
        matches_lost=int(cellF.value)
        sets_won=int(cellG.value)
        sets_lost=int(cellH.value)
        wildcard_state=int(cellI.value)
        challenges_given_state=int(cellJ.value)
        challenges_taken_state=int(cellK.value)
        challenges_given=int(cellL.value)
        challenges_taken=int(cellM.value)
        challenges_final=int(cellN.value)
        challenges_final_state=int(cellO.value)
        player_data_main.append(Player(name,surname,age,matches_played,matches_won,matches_lost,sets_won,sets_lost,wildcard_state,challenges_given_state,challenges_taken_state,challenges_given,challenges_taken,challenges_final,challenges_final_state))
    return
#################################################################    
############ΓΡΑΦΕΙ ΣΤΗΝ CH_OUT_MATCHES_MAIN                 #####
#################################################################
def create_class_challenge_match(ch_giver_serial,ch_taker_serial): #ΔΗΜΙΟΥΡΓΕΙ ΤΗΝ ΚΛΑΣΗ CHALLENGE MATCH ΣΤΗΝ ΛΙΣΤΑ CH_OUT_MATCHES_MAIN
        name_giver = player_data_main[ch_giver_serial].name
        name_taker = player_data_main[ch_taker_serial].name
        surname_giver = player_data_main[ch_giver_serial].surname
        surname_taker = player_data_main[ch_taker_serial].surname
        ch_out_matches.append(name_giver)
        ch_out_matches.append(surname_giver)
        ch_out_matches.append(ch_giver_serial)
        ch_out_matches.append(name_taker)
        ch_out_matches.append(surname_taker)
        ch_out_matches.append(ch_taker_serial)
        ch_out_matches_main.append(Challenge_Match(name_taker,surname_taker,ch_taker_serial,name_giver,surname_giver,ch_giver_serial))
        return
def load_class_out_match(filename,list): # ΦΟΡΤΩΝΕΙ ΑΠΟ ΤΟ ΑΡΧΕΙΟ EXCEL ΤΗΝ ΚΛΑΣΗ CHALLENGE MATCH ΣΤΗΝ ΛΙΣΤΑ CHA_OUT_MATCHES_MAIN
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    max_row = sheet.max_row
    for i in range(2, max_row+1):
        cellA = sheet.cell(i,1)
        cellB = sheet.cell(i,2)
        cellC = sheet.cell(i,3)
        cellD = sheet.cell(i,4)
        cellE = sheet.cell(i,5)
        cellF = sheet.cell(i,6)
        name_taker = cellA.value
        surname_taker = cellB.value
        ch_taker_serial = int(cellC.value)
        name_giver = cellD.value
        surname_giver = cellE.value
        ch_giver_serial = int(cellF.value)
        ch_out_matches_main.append(Challenge_Match(name_taker,surname_taker,ch_taker_serial,name_giver,surname_giver,ch_giver_serial))
    return
#####################################################################
### ΓΡΑΦΕΙ ΣΤΗΝ CH_VALID_MATCHES KAI CH_VALID_MATCHES_MAIN###########
#####################################################################
def add_valid_challenge_match(ch_giver_serial,ch_taker_serial): # ΓΡΑΦΕΙ ΣΤΗΝ VALID_MATCHES_MAIN ΤΑ ΕΓΚΥΡΑ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ
    name_giver = player_data_main[ch_giver_serial].name
    name_taker = player_data_main[ch_taker_serial].name
    surname_giver = player_data_main[ch_giver_serial].surname
    surname_taker = player_data_main[ch_taker_serial].surname
    ch_valid_matches.append(name_giver)
    ch_valid_matches.append(surname_giver)
    ch_valid_matches.append(ch_giver_serial)
    ch_valid_matches.append(name_taker)
    ch_valid_matches.append(surname_taker)
    ch_valid_matches.append(ch_taker_serial)
    ch_valid_matches_main.append(Challenge_Match(name_taker,surname_taker,ch_taker_serial,name_giver,surname_giver,ch_giver_serial))
    return
def load_class_valid_match(filename,list): # ΦΟΡΤΩΝΕΙ ΑΠΟ ΤΟ ΑΡΧΕΙΟ EXCEL ΤΑ ΕΓΚΥΡΑ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    max_row = sheet.max_row
    for i in range(2, max_row+1):
        cellA = sheet.cell(i,1)
        cellB = sheet.cell(i,2)
        cellC = sheet.cell(i,3)
        cellD = sheet.cell(i,4)
        cellE = sheet.cell(i,5)
        cellF = sheet.cell(i,6)
        name_taker = cellA.value
        surname_taker = cellB.value
        ch_taker_serial = int(cellC.value)
        name_giver = cellD.value
        surname_giver = cellE.value
        ch_giver_serial = int(cellF.value)
        ch_out_matches_main.append(Challenge_Match(name_taker,surname_taker,ch_taker_serial,name_giver,surname_giver,ch_giver_serial))  
    return
###ΕΓΡΑΦΗ ΝΕΟΥ ΠΑΙΚΤΗ###
def add_class(Name,Surname,Age): # ΚΑΝΕΙ ΤΗΝ ΕΓΡΑΦΗ ΕΝΟΣ ΝΕΟΥ ΠΑΙΚΤΗ ΣΤΗΝ PLAYER_DATA ΚΑΘΩΣ ΚΑΙ ΣΤΗΝ PLAYER_DATA_MAIN
    player_data.append(Name)
    player_data.append(Surname)
    player_data.append(Age)
    player_data.append(0)
    player_data.append(0)
    player_data.append(0)
    player_data.append(0)
    player_data.append(0)
    player_data.append(1)
    player_data.append(0)
    player_data.append(0)
    player_data.append(0)
    player_data.append(0)
    player_data.append(0)
    player_data.append(1)
    player_data_main.append(Player(name=Name,surname=Surname,age=Age,matches_played=0,matches_won=0, matches_lost=0, sets_won=0, sets_lost=0, wildcard_state=1, challenges_given_state=0, challenges_taken_state=0, challenges_given=0, challenges_taken=0, challenges_final=0, challenges_final_state=1))
    return
#####################################################
###ΔΙΑΓΡΑΦΗ ΠΑΙΧΤΗ###
def del_list(data,heads,ranking_position):##ΣΒΗΝΕΙ ΑΠΟ ΤΗΝ ΛΙΣΤΑ ΕΙΣΟΔΟΥ ΤΟΝ ΠΑΙΚΤΗ ΠΟΥ ΠΕΡΝΑΜΕ ΩΣ ΕΙΣΟΔΟ Η ΕΠΙΚΕΦΑΛΙΔΕΣ ΚΑΘΟΡΙΖΟΥΝ ΤΟ ΜΗΚΟΣ ΚΑΙ ΤΟ ΠΛΑΤΟΣ ΤΟΥ ΠΙΝΑΚΑ ΑΥΤΟΥ(HEADS)
  
    arr = np.array(data)
    
    N = int(len(data)/len(heads))
    M = len(heads)
    
    multi_dim = np.reshape(arr,(N,M))
    new_multi_dim = np.delete(multi_dim,ranking_position,1)
    data = new_multi_dim.flatten()
    
    return
    
def del_classes(list,ranking_position):##ΣΒΗΝΕΙ ΑΠΟ ΤΗΝ ΛΙΣΤΑ ΕΙΣΟΔΟΥ ΕΝΑ ΠΑΙΚΤΗ ΠΟΥ ΑΝΑΛΟΓΕΙ ΣΤΗΝ ΚΑΤΑΤΑΞΗ
    del list[ranking_position]
##################################################################################
###################ΛΟΓΙΚΗ ΠΡΟΚΛΗΣΕΩΝ##############################################
###TRUE ΕΓΚΥΡΗ ΠΡΟΚΛΗΣΗ                                                          #
###FALSE ΜΗ ΕΓΚΥΡΗ                                                               #
### Η ΚΥΡΙΑ ΛΟΓΙΚΗ ΓΙΑ ΤΟ ΕΑΝ ΜΠΟΡΕΙ ΑΝ ΔΟΘΕΙ ΜΙΑ ΠΡΟΚΛΗΣΗ                       #
##################################################################################
##################################################################################
### ΑΣΤΕΡΙΣΚΟΣ ΝΑ ΤΟ ΚΟΙΤΑΞΩ###
### Η  ΛΟΓΙΚΗ ΑΥΤΗΣ ΤΗΣ ΣΥΝΑΡΤΗΣΗΣ ΕΙΝΑΙ ΟΤΙ ΕΑΝ Ο ΠΑΙΚΤΗΣ ΕΧΕΙ ΜΠΑΛΑΝΤΕΡ ΚΑΙ ΜΠΟΡΕΙ ΝΑ ΔΩΣΕΙ ΑΛΛΕΣ ΠΡΟΚΛΗΣΕΙΣ ΚΑΙ Ο ΣΤΟΧΟΣ ΜΠΟΡΕΙ ΝΑ ΑΠΟΔΕΚΤΕΙ ΤΟΤΕ ΕΠΙΣΤΡΕΦΕΙ 1 ΑΛΛΙΩΣ ΕΠΙΣΤΡΕΦΕΙ 0   
def MAIN_LOGIC_OF_CHECK_CHALLENGE_WILD(giver,taker): ### MAIN FUCTION TO CHECK FOR NEW CHALLENGES (IF THE GIVER HAS WILDCARD AND CAN GIVE MORE CHALLENGES AND THE TAKER CAN ACCEPT MORE CHALLENGES)
    player_data_main[giver].alter_challenges_given_state() # ΚΑΛΕΙ ΤΗΝ ΣΥΝΑΡΤΗΣΗ ΚΛΑΣΗΣ ΠΟΥ ΕΛΕΓΧΕΙ ΤΙΣ ΠΡΟΚΛΗΣΕΙΣ ΠΟΥ ΔΕΚΤΗΚΕ Ο ΠΑΙΚΤΗΣ ΑΠΟΣΤΟΛΕΑΣ ΤΗΣ ΠΡΟΚΛΗΣΗΣ
    player_data_main[taker].alter_challenges_taken_state() # ΚΑΛΕΙ ΤΗΝ ΣΥΝΑΡΤΗΣΗ ΚΛΑΣΗΣ ΠΟΥ ΕΛΕΓΧΕΙ ΤΙΣ ΠΡΟΚΛΗΣΕΙΣ ΠΟΥ ΜΠΟΡΕΙ ΝΑ ΔΕΚΤΕΙ Ο ΠΑΙΚΤΗΣ ΣΤΟΧΟΣ ΤΗΣ ΠΡΟΚΛΗΣΗΣ
    player_data_main[giver].alter_challenges_final_state() # ΚΑΛΕΙ ΤΗΝ ΣΥΝΑΡΤΗΣΗ ΚΛΑΣΗΣ ΠΟΥ ΕΛΕΓΧΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΕΝΕΡΓΩΝ ΠΡΟΚΛΗΣΕΩΝ ΤΟΥ ΠΑΙΚΤΗ ΠΟΥ ΕΣΤΕΙΛΕ ΤΗΝ ΠΡΟΚΛΗΣΗ
    if(player_data_main[giver].wildcard_state==1 and player_data_main[giver].challenges_given_state==1 and player_data_main[giver].challenges_final_state==1 and player_data_main[taker].challenges_taken_state==1 and player_data_main[taker].challenges_final_state==1 and giver>taker):
        return 1 ## TRUE 
    
    return 0    ##FALSE
### Η ΛΟΓΙΚΗ ΑΥΤΗΣ ΤΗΣ ΣΥΝΑΡΤΗΣΗΣ ΕΙΝΑΙ ΟΤΙ ΕΑΝ Ο ΠΑΙΚΤΗΣ ΠΟΥ ΚΑΝΕΙ ΤΗΝ ΠΡΟΚΛΗΣΗ ΔΕΝ ΕΧΕΙ ΜΠΑΛΑΝΤΕΡ ΑΛΛΑ Η ΠΡΟΚΛΗΣΗ ΕΙΝΑΙ ΕΚΓΥΡΗ ΛΟΓΩ ΚΑΤΑΤΑΞΗΣ(ΑΠΟΣΤΑΣΗΣ ΤΩΝ ΔΥΟ ΠΑΙΚΤΩΝ) ΚΑΙ Ο ΑΠΟΣΤΟΛΕΑΣ ΜΠΟΡΕΙ ΝΑ ΔΩΣΕΙ ΠΡΟΚΛΗΣΗ ΚΑΙ Ο ΣΤΟΧΟΣ ΝΑ ΔΕΚΤΕΙ
def MAIN_LOGIC_OF_CHECK_CHALLENGE_VALID(giver,taker):
    player_data_main[giver].alter_challenges_final_state() # ΚΑΛΕΙ ΤΗΝ ΣΥΝΑΡΤΗΣΗ ΚΛΑΣΗΣ ΠΟΥ ΕΛΕΓΧΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΕΝΕΡΓΩΝ ΠΡΟΚΛΗΣΕΩΝ ΓΙΑ ΤΟΝ ΑΠΟΣΤΟΛΕΑ
    player_data_main[giver].alter_challenges_given_state() #ΚΑΛΕΙ ΤΗΝ ΣΥΝΑΡΤΗΣΗ ΚΛΑΣΗΣ ΠΟΥ ΕΛΕΓΧΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΑΠΟΣΤΑΛΜΕΝΩΝ ΠΡΟΚΛΗΣΕΩΝ ΓΙΑ ΤΟΝ ΑΠΟΣΤΟΛΕΑ
    player_data_main[taker].alter_challenges_taken_state() #ΚΑΛΕΙ ΤΗΝ ΣΥΝΑΡΤΗΣΗ ΚΛΑΣΗΣ ΠΟΥ ΕΛΕΓΧΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΑΠΟΔΕΚΤΩΝ ΠΡΟΚΛΗΣΕΩΝ ΓΙΑ ΤΟΝ ΣΤΟΧΟ ΤΗΣ ΠΡΟΚΛΗΣΗΣ
    if(player_data_main[giver].wildcard_state==0 and giver>taker and abs(giver-taker)<=MAX_RANKING_CHALLENGE and player_data_main[giver].challenges_given_state==1 and player_data_main[taker].challenges_taken_state==1):
        return 1 ## TRUE 
    
    return 0 ## FALSE 

def MAIN_LOGIC_CHK_DUP_CHAL(position1,position2): ##ΕΛΕΓΧΕΙ ΓΙΑ ΕΠΑΝΑΛΑΜΒΑΝΟΜΕΝΕΣ ΠΡΟΚΛΗΣΕΙΣ ΔΗΛΑΔΗ ΕΑΝ ΕΧΕΙ ΔΟΘΕΙ ΗΔΗ ΠΡΟΚΛΗΣΗ ΣΤΟΝ ΠΑΙΚΤΗ ΑΥΤΟ Ο ΕΛΕΓΧΟΣ ΓΙΝΕΤΑΙ ΒΑΣΗ ΟΝΟΜΑΤΩΝ
    for i in range(len(ch_out_matches_main)):
        if((ch_out_matches_main[i].giver_serial==position1 and ch_out_matches_main[i].taker_serial==position2) or (ch_out_matches_main[i].giver_serial==position2 and ch_out_matches_main[i].taker_serial==position1)):
            return 0 ## FALSE 
    return 1 ##TRUE
        
def MAIN_LOGIC_ALL(giver,taker): # ΚΥΡΙΑ ΣΥΝΑΡΤΗΣΗ ΕΛΕΓΧΟΥ  ΕΛΕΓΧΕΙ ΜΕ ΒΑΣΕΙ ΤΙΣ ΠΑΡΑΠΑΝΩ ΣΥΝΑΡΤΗΣΕΙΣ
    if(MAIN_LOGIC_OF_CHECK_CHALLENGE_WILD(giver,taker)==1 and MAIN_LOGIC_CHK_DUP_CHAL(giver,taker)==1):
        ### ΕΑΝ Η ΠΡΟΚΛΗΣΗ ΜΠΟΡΕΙ ΝΑ ΔΟΘΕΙ ΜΕ ΒΑΣΗ ΤΟΝ ΜΠΑΛΑΝΤΕΡ ΚΑΙ ΔΕΝ ΕΙΝΑΙ ΔΙΠΛΗ
        return 1 ## TRUE
    if(MAIN_LOGIC_OF_CHECK_CHALLENGE_VALID(giver,taker)==1 and MAIN_LOGIC_CHK_DUP_CHAL(giver,taker)==1):
        ###ΕΑΝ Η ΠΡΟΚΛΗΣΗ ΜΠΟΡΕΙ ΝΑ ΔΟΘΕΙ ΜΕ ΒΑΣΗ ΤΗΝ ΚΑΤΑΤΑΞΗ ΚΑΙ ΔΕΝ ΕΙΝΑΙ ΔΙΠΛΗ
        return 1 ## TRUE
   
    return 0 ##FALSE
##############################################################################
###ΣΥΝΑΡΤΗΣΗ ΠΟΥ ΚΑΝΕΙ ΑΝΤΑΛΛΑΓΗ                                        ######
##############################################################################

    
def SWAP(data,winner,loser):# Η ΣΥΝΑΡΤΗΣΗ ΑΥΤΗ ΔΕΧΕΤΕ ΜΙΑ ΛΙΣΤΑ ΚΑΙ ΔΥΟ ΑΡΙΘΜΟΥΣ ΚΑΤΑΤΑΞΗΣ ΚΑΙ ΕΠΙΣΤΡΕΦΕΙ ΤΟΝ ΠΙΝΑΚΑ ΜΕ ΒΑΣΗ ΤΗΝ ΑΛΛΑΓΗ ΣΤΗΝ ΚΑΤΑΤΑΞΗ
    base = data[loser] # ΑΠΟΘΗΚΕΥΟΥΜΕ ΤΟΝ ΠΑΙΚΤΗ ΠΟΥ ΗΤΤΗΘΗΚΕ 
    data[loser] = data[winner] # ΣΤΗΝ ΘΕΣΗ ΤΟΥ ΗΤΤΗΜΕΝΟΥ ΠΕΡΝΑΕΙ Ο ΝΙΚΗΤΗΣ
    TEMP = []# ΤΟΠΙΚΕΣ ΜΕΤΑΒΛΗΤΕΣ ΠΟΥ ΣΩΖΟΥΝ ΤΑ ΣΤΟΙΧΕΙΑ ΤΗΣ ΛΙΣΤΑΣ
    temp = []
    for i in range(loser+1,len(data)):# ΕΠΑΝΑΛΗΨΗ ΑΠΟ ΤΗΝ ΘΕΣΗ ΤΟΥ ΗΤΤΗΜΕΝΟΥ ΑΥΞΗΜΕΝΗ ΚΑΤΑ ΜΙΑ ΘΕΣΗ ΕΩΣ ΤΟ ΤΕΛΟΣ ΤΙΣ ΛΙΣΤΑΣ
        if(i == loser+1): # ΕΑΝ ΤΟ Ι ΕΙΝΑΙ ΙΣΟ ΜΕ ΤΗΝ ΘΕΣΗ ΜΕΤΑ ΤΟΝ ΧΑΜΕΝΟ
           TEMP = data[i]
           temp = data[i]
           data[i] = base # ΠΕΡΝΑΜΕ ΤΟΝ ΧΑΜΕΝΟ ΜΙΑ ΘΕΣΗ ΠΙΟ ΚΑΤΩ
        if(i%2==0 and i !=loser+1): # ΤΟ ΙΔΙΟ ΚΑΝΟΥΜΕ ΚΑΙ ΓΙΑ ΚΑΘΕ ΑΛΛΗ ΘΕΣΗ
            TEMP = data[i]
            data[i] = temp
        if(i%2!=0 and i != loser+1):
            temp = data[i]
            data[i]=TEMP
    return    
####################################################################
### ΜΕΝΟΥ###########################################################
####################################################################
###ΑΥΤΗ Η ΚΛΑΣΗ ΕΙΝΑΙ ΤΟ ΚΥΡΙΟ ΜΕΝΟΥ###
class MAIN(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen',True)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}")
        self.text=tkinter.Text(self,bg="black",fg="white",font=("System",12,"bold"),bd=8,yscrollcommand=True,xscrollcommand=True,width=120,height=50)
        self.text.pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Button(self,height=1,width=30,text = "Εξοδος",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.terminate).pack(anchor=tkinter.SW,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=30,text = "Ρυθμίσεις",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.settings).pack(anchor=tkinter.SW,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=30,text ="Εκτύπωση Κατάταξης",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.print_ranking).pack(anchor=tkinter.SE,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=30,text ="Εκτύπωση Κατάταξης Με Στατιστικά",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.print_ranking_stats).pack(anchor=tkinter.SE,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=40,text ="Εκτύπωση Εκρρεμών Μάτς Πρόκλησης",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.print_out_ch_matches).pack(anchor=tkinter.SE,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=40,text ="Εκτύπωση Ενεργών Μάτς Πρόκλησης",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.print_valid_ch_matches).pack(anchor=tkinter.SE,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=40,text ="Διαχείριση Εκρεμών Μάτς Πρόκλησης",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.ch_out_man).pack(anchor=tkinter.SE,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=40,text ="Ενημέρωση Ενεργών Μάτς Πρόκλησης ",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.ch_valid_man).pack(anchor=tkinter.SE,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=30,text ="Νέο Μάτς Πρόκλησης",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.new_ch_match).pack(anchor=tkinter.SE,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=30,text ="Διαγραφή Παίχτη",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.del_player).pack(anchor=tkinter.SE,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=30,text ="Εγγραφή Νέου Παίχτη",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.add_player).pack(anchor=tkinter.SE,side=tkinter.LEFT)
    
    ####ΚΟΥΜΠΙ ΤΕΡΜΑΤΙΣΜΟΥ####
    def terminate(self):
        global filename_player_data
        global filename_out_ch
        global filename_valid_ch
        write_excel_file(filename_player_data,player_data,heads_players)
        write_excel_file(filename_out_ch,ch_out_matches,heads_ch_out_match)
        write_excel_file(filename_valid_ch,ch_valid_matches,heads_ch_valid_match)
        root.destroy()
        
   
    ###ΤΥΠΩΝΕΙ ΤΗΝ ΒΑΣΙΚΗ ΚΑΤΑΤΑΞΗ###
    def print_ranking(self): 
        self.text.configure(state = 'normal')
        self.text.delete('1.0','end')
        for index in range(len(player_data_main)):
            self.text.insert(tkinter.INSERT,str(index+1)+'\t')
            self.text.insert(tkinter.INSERT,player_data_main[index].__str__()+'\n')
        self.text.configure(state = 'disabled')
    
    ###TYΠΩΝΕΙ ΤΗΝ ΚΑΤΑΤΑΞΗ ΜΕ ΣΤΑΤΙΣΤΙΚΑ###
    def print_ranking_stats(self):
        self.text.configure(state = 'normal')
        self.text.delete('1.0','end')
        for index in range(len(player_data_main)):
            self.text.insert(tkinter.INSERT,str(index+1)+'\t')
            self.text.insert(tkinter.INSERT,player_data_main[index].__str__stats__()+'\n')
        self.text.configure(state = 'disabled')

    ###ΤΥΠΩΝΕΙ ΤΑ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ ΠΟΥ ΕΙΝΑΙ ΕΚΡΕΜΗ###
    def print_out_ch_matches(self):
        self.text.configure(state = 'normal')
        self.text.delete('1.0','end')
        for i in range(len(ch_out_matches_main)):
             self.text.insert(tkinter.INSERT,"Πρόκληση"+'\t'+ str(i+1)+'η'+'\t' + ch_out_matches_main[i].__str__()+'\n')
        self.text.configure(state = 'disabled')

    ###ΤΥΠΩΝΕΙ ΤΑ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ ΠΟΥ ΕΙΝΑΙ ΕΝΕΡΓΑ###
    def print_valid_ch_matches(self):
        self.text.configure(state='normal')
        self.text.delete('1.0','end')
        for i in range(len(ch_valid_matches_main)):
            self.text.insert(tkinter.INSERT,"Κατάταξη"+'\t'+str(i+1)+ch_valid_matches_main[i].__str__()+'\n')
        self.text.configure(state = 'disabled')
    ###ΔΙΑΧΕΙΡΙΣΗ ΕΚΚΡΕΜΩΝ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ###
    def ch_out_man(self):
        top = OUTSTANDING_CHALLENGE_MATCH(self)
        top.grab_set()
    ###ΕΝΗΜΕΡΩΣΗ ΕΝΕΡΓΩΝ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ###
    def ch_valid_man(self):
        top = BRIEF_CHALLENGE_MATCH(self)
        top.grab_set()
    ###ΝΕΟ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ###
    def new_ch_match(self):
        top = NEW_CHALLENGE_MATCH(self)
        top.grab_set()
    ###ΔΙΑΓΡΑΦΗ ΠΑΙΚΤΗ###
    def del_player(self):
        top = DEL_PLAYER(self)
        top.grab_set()
    ###ΕΓΡΑΦΗ ΝΕΟΥ ΠΑΙΧΤΗ###
    def add_player(self):
        top = ADD_PLAYER(self)
        top.grab_set()
    ###ΡΥΘΜΙΣΕΙΣ###
    def settings(self):
        top = SETTINGS(self)
        top.grab_set()

###ΚΛΑΣΗ ΥΠΟ ΜΕΝΟΥ ΑΠΟΔΟΧΗ ΕΙΣΟΔΟΥ###

class CONFIRMED(tkinter.Toplevel): 
    def __init__(self,parent): 
        super().__init__(parent)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width//10}x{self.screen_height//10}+{self.screen_width//2}+{self.screen_height//2}")
        tkinter.Label(self,text="Αποδοχή",fg="green",font=("System",12)).pack()
        tkinter.Button(self,text='Επιστροφή',activebackground="white",activeforeground="red",fg="black",font=("System",10),highlightcolor="black",padx=10,pady=10,command=self.destroy).pack(anchor=tkinter.S,side=tkinter.BOTTOM)

###ΚΛΑΣΗ ΥΠΟ ΜΕΝΟΥ ΑΠΟΡΡΙΨΗ ΕΙΣΟΔΟΥ###
class FAILED(tkinter.Toplevel): 
    def __init__(self,parent): 
        super().__init__(parent)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width//10}x{self.screen_height//10}+{self.screen_width//2}+{self.screen_height//2}")
        tkinter.Label(self,text="Απόρριψη",fg="green",font=("System",12)).pack()
        tkinter.Button(self,text='Επιστροφή',activebackground="white",activeforeground="red",fg="black",font=("System",10),highlightcolor="black",padx=10,pady=10,command=self.destroy).pack(anchor=tkinter.S,side=tkinter.BOTTOM)

###ΚΛΑΣΗ ΥΠΟ ΜΕΝΟΥ ΕΓΓΡΑΦΗ ΝΕΟΥ ΠΑΙΚΤΗ###
class ADD_PLAYER(tkinter.Toplevel):
    def __init__(self,parent): 
        super().__init__(parent)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width//6}x{self.screen_height//6}+{self.screen_width//2}+{self.screen_height//2}")
        self.name = tkinter.StringVar()
        self.surname = tkinter.StringVar()
        self.age = tkinter.IntVar(value=18)
        tkinter.Label(self,text="Ονομα",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.name).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Επώνυμο",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.surname).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Ηλικία",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.age).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Button(self,height=1,width=30,text = "Επιστροφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.destroy).pack(anchor=tkinter.SW,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=30,text = "Εγγραφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.confirm).pack(anchor=tkinter.SW,side=tkinter.RIGHT)
###ΕΠΙΒΕΒΑΙΩΣΗ ΠΡΟΣΘΗΚΗΣ ΠΑΙΚΤΗ###
    def confirm(self):
        try:
                name=self.name.get()
                surname=self.surname.get()
                age=self.age.get()

                if(len(name)>=1 and len(surname)>=1 and age>=18):
                    add_class(name,surname,age) #ΠΡΟΣΘΕΤΕΙ ΤΟΝ ΠΑΙΧΤΗ ΕΑΝ ΕΙΝΑΙ ΑΝΩ ΤΩΝ 18
                    top = CONFIRMED(self)
                    top.grab_set()
        
        except:
                top = FAILED(self)
                top.grab_set()

###ΚΛΑΣΗ ΥΠΟ ΜΕΝΟΥ ΔΙΑΓΡΑΦΗ ΠΑΙΚΤΗ####
class DEL_PLAYER(tkinter.Toplevel):
    def __init__(self,parent): 
        super().__init__(parent)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width//6}x{self.screen_height//6}+{self.screen_width//2}+{self.screen_height//2}")
        self.variable_del = tkinter.IntVar()
        tkinter.Label(self,text="Αριθμός Κατάταξης",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.variable_del).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Button(self,height=1,width=30,text = "Επιστροφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.destroy).pack(anchor=tkinter.SW,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=30,text = "Διαγραφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.confirm_del).pack(anchor=tkinter.SW,side=tkinter.RIGHT)
###EΠΙΒΕΒΑΙΩΣΗ ΔΙΑΓΡΑΦΗ ΠΑΙΚΤΗ###
    def confirm_del(self):
       try:
            var_del_player = self.variable_del.get()
            if(var_del_player>=1 and var_del_player<=(len(player_data_main)+1)):
                    del_classes(player_data_main,var_del_player-1) #ΣΒΗΝΕΙ ΤΟΝ ΠΑΙΧΤΗ
                    del_list(player_data,heads_players,var_del_player-1)
                    top = CONFIRMED(self)
                    top.grab_set()
            else:
                top = FAILED(self)
                top.grab_set()               
                
       except:
           top = FAILED(self)
           top.grab_set()
             
###ΚΛΑΣΗ ΥΠΟΜΕΝΟΥ ΡΥΘΜΙΣΕΙΣ ##
class SETTINGS(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width//6}x{self.screen_height//6}+{self.screen_width//2}+{self.screen_height//2}")
        self.wildcard = tkinter.IntVar()
        self.max_ch_ranking = tkinter.IntVar()
        self.max_in = tkinter.IntVar()
        self.max_out = tkinter.IntVar()
        self.max_active = tkinter.IntVar()  
        tkinter.Label(self,text="Μάτς για Μπαλαντέρ",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.wildcard).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Απόσταση στην Κατάταξη",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.max_ch_ranking).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Προκλήσεις Εξόδου",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.max_out).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Προκλήσεις Εισόδου",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.max_in).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Mέγιστος αριθμός Επιτρεπώμενω Ενεργών Προκήσεων",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.max_active).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Button(self,height=1,width=10,text = "Επιστροφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.destroy).pack(anchor=tkinter.SW,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=15,text = "Φόρτωση Αρχείου",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.load_from_file).pack(anchor=tkinter.SW,side=tkinter.RIGHT)
        tkinter.Button(self,height=1,width=10,text = "Εγγραφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.define_settings).pack(anchor=tkinter.SW,side=tkinter.RIGHT)
### ΡΥΘΜΙΣΕΙΣ###
    def define_settings(self):
        global WILDCARD
        global MAX_RANKING_CHALLENGE
        global MAX_CHALLENGES_IN
        global MAX_CHALLENGES_OUT
        global MAX_ACTIVE_CHALLENGES
        try:
            WILDCARD = self.wildcard.get()
            MAX_RANKING_CHALLENGE = self.max_ch_ranking.get()
            MAX_CHALLENGES_IN = self.max_in.get()
            MAX_CHALLENGES_OUT = self.max_out.get()
            MAX_ACTIVE_CHALLENGES = self.max_active.get()
            top = CONFIRMED(self)
            top.grab_set()
        except:
            top = FAILED(self)
            top.grab_set()
        return WILDCARD,MAX_RANKING_CHALLENGE,MAX_CHALLENGES_IN,MAX_CHALLENGES_OUT
    def load_from_file(self):
        global filename_player_data
        global filename_out_ch
        global filename_valid_ch
        filename_player_data= tkinter.filedialog.askopenfilename(title='Αρχείο Κατάταξης')
        filename_out_ch = tkinter.filedialog.askopenfilename(title='Εκρεμη Μάτς Πρόκλησης')
        filename_valid_ch = tkinter.filedialog.askopenfilename(title='Ενεργά Μάτς Πρόκλησης')
        open_excel_file(filename_player_data,player_data)
        open_excel_file(filename_out_ch,ch_out_matches)
        open_excel_file(filename_valid_ch,ch_valid_matches)
        load_class_player(filename_player_data,player_data)
        load_class_out_match(filename_out_ch,ch_out_matches)
        load_class_valid_match(filename_valid_ch,ch_valid_matches)
        return
       
    
###ΚΛΑΣΗ ΥΠΟΜΕΝΟΥ ΝΕΟ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ###
class NEW_CHALLENGE_MATCH(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width//6}x{self.screen_height//6}+{self.screen_width//2}+{self.screen_height//2}")
        self.challenger = tkinter.IntVar()
        self.champion = tkinter.IntVar()
        tkinter.Label(self,text="Παίκτης που προκαλεί",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.challenger).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Παίκης αποδέκτης πρόκλησης",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.champion).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Button(self,height=1,width=10,text = "Επιστροφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.destroy).pack(anchor=tkinter.SW,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=10,text = "Εγγραφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.confirm_ch_match).pack(anchor=tkinter.SW,side=tkinter.RIGHT)
    def confirm_ch_match(self):
        try:
            giver = self.challenger.get()
            taker = self.champion.get()

            if( giver >=1 and giver <= (len(player_data_main)+1)  and taker >=1 and taker <=len(player_data_main)+1):
           ### ΕΛΕΓΧΕΙ ΑΝ ΟΙ ΑΡΙΘΜΟΙ ΕΙΝΑΙ ΣΤΗΝ ΕΠΙΤΡΕΠΟΜΕΝΗ ΑΠΟΣΤΑΣΗ
                if(MAIN_LOGIC_ALL(giver-1,taker-1)==1): #ΑΝ ΜΠΟΡΕΙ ΝΑ ΔΟΘΕΙ ΠΡΟΚΛΗΣΗ
                    
                    player_data_main[giver-1].increase_challenges_given()   #ΑΥΞΑΝΕΙ ΤΙΣ ΠΡΟΚΛΗΣΕΙΣ ΠΟΥ ΕΔΩΣΕ Ο ΠΡΟΚΛΗΤΗΣ
                    
                    player_data_main[taker-1].increase_challenges_taken()   #ΑΥΞΑΝΕΙ ΤΙΣ ΠΡΟΚΛΗΣΕΙΣ ΠΟΥ ΔΕΧΤΗΚΕ ΑΥΤΟΣ ΠΟΥ ΠΡΟΚΛΗΘΗΚΕ
                    
                    player_data_main[giver-1].alter_challenges_given_state() #ΕΛΕΓΧΕΙ ΤΑ ΟΡΙΑ ΠΡΟΚΛΗΣΕΩΝ
                    
                    player_data_main[taker-1].alter_challenges_taken_state() #ΕΛΕΓΧΕΙ ΤΑ ΟΡΙΑ ΠΡΟΚΛΗΣΕΩΝ
                    
                    player_data_main[giver-1].alter_wildcard_state()            #ΑΛΛΑΖΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΤΟΥ ΜΠΑΛΑΝΤΕΡ
                    
                    player_data_main[giver-1].increase_challenges_final()       #ΑΥΞΑΝΕΙ ΤΙΣ ΠΡΟΚΛΗΣΕΙΣ ΑΠΟΔΕΚΤΕΣ ΤΟΥ ΔΟΤΗ
                    
                    player_data_main[giver-1].alter_challenges_final_state()    #ΑΛΛΑΖΕΙ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΑΠΟΔΕΚΤΩΝ ΠΡΟΚΛΗΣΕΩΝ ΓΙΑ ΤΟΝ ΔΟΤΗ
                    
                    create_class_challenge_match((taker-1),(giver-1)) # ΓΡΑΦΕΙ ΤΟ ΜΑΤΣ ΠΡΟΚΛΗΣHΣ ΣΤΟΝ ΠΙΝΑΚΑ 
                    top = CONFIRMED(self)
                    top.grab_set()
                    
                else:
                    top = FAILED(self)
                    top.grab_set()
                    
                  
            else:
                top = FAILED(self)
                top.grab_set()
                
        except:
               top = FAILED(self)
               top.grab_set()
               

###ΚΛΑΣΗ ΥΠΟΜΕΝΟΥ ΕΝΗΜΕΡΩΣΗ ΕΝΕΡΓΩΝ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ###
class BRIEF_CHALLENGE_MATCH(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width//6}x{self.screen_height//6}+{self.screen_width//2}+{self.screen_height//2}")
        self.serial = tkinter.IntVar()
        self.winner = tkinter.IntVar()
        self.loser = tkinter.IntVar()
        self.sets_winner = tkinter.IntVar()
        self.sets_loser = tkinter.IntVar()
        tkinter.Label(self,text="Αριθμός μάτς κατάταξης προς ενημέρωση",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.serial).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Αριθμός κατάταξης παίχτη που νίκησε",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.winner).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Σετ που πήρε ο Νικητής",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.sets_winner).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Αριθμός κατάταξης παίχτη που ηττήθηκε",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.loser).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Label(self,text="Σετ που πήρε ο Ηττημένος",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.sets_loser).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Button(self,height=1,width=10,text = "Επιστροφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.destroy).pack(anchor=tkinter.SW,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=10,text = "Εγγραφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.brief_match).pack(anchor=tkinter.SW,side=tkinter.RIGHT)
    def brief_match(self):
        try:
            serial = self.serial.get()
            winner = self.winner.get()
            loser = self.loser.get()
            sets_winner = self.sets_winner.get()
            sets_loser = self.sets_loser.get()
        
            if(sets_winner>=1 and sets_winner<=POINT_SET_MATCH and sets_loser>=1 and sets_loser<=POINT_SET_MATCH and sets_winner>sets_loser and winner>=1 and winner<=len(player_data_main)+1 and loser>=1 and loser<=len(player_data_main)+1 and serial>=1 and serial<=(len(ch_valid_matches_main)+1)):#EΑΝ ΟΙ ΑΡΙΘΜΟΙ ΥΠΟΚΕΙΝΤΑΙ ΣΤΟΥΣ ΚΑΝΟΝΕΣ ΓΙΑ ΤΑ ΠΑΙΧΝΔΙΑ
                player_data_main[winner-1].increase_sets_won(sets_winner) #ΣΕΤ ΑΥΞΗΣΗ
                
                player_data_main[loser-1].increase_sets_won(sets_loser)#ΣΕΤ ΑΥΞΗΣΗ
                
                player_data_main[winner-1].increase_sets_lost(sets_loser)#ΣΕΤ ΑΥΞΗΣΗ
                
                player_data_main[loser-1].increase_sets_lost(sets_winner)#ΣΕΤ ΑΥΞΗΣΗ
                
                player_data_main[winner-1].increase_matches_played()#ΜΑΤΣ ΑΥΞΗΣΗ
                  
                player_data_main[loser-1].increase_matches_played()#ΜΑΤΣ ΑΥΞΗΣΗ
                
                player_data_main[winner-1].increase_matches_won()#ΜΑΤΣ ΝΙΚΕΣ ΑΥΞΗΣΗ
                
                player_data_main[loser-1].increase_matches_lost()#ΜΑΤΣ ΗΤΤΕΣ ΑΥΞΗΣΗ
                
                player_data_main[winner-1].alter_wildcard_state()#ΑΛΛΑΓΗ ΤΟΥ ΜΠΑΛΑΝΤΕΡ
                
                player_data_main[loser-1].alter_wildcard_state()# ΑΛΛΑΓΗ ΤΟΥ ΜΠΑΛΑΝΤΕΡ
                
                player_data_main[winner-1].decrease_challenges_final()#ΑΛΛΑΓΗ ΤΗΣ ΚΑΤΑΣΤΑΣΗΣ ΕΝΕΡΓΩΝ ΠΡΟΚΛΗΣΕΩΝ
                
                player_data_main[loser-1].decrease_challenges_final() # ΜΕΙΩΣΗ ΤΟΝ ΕΝΕΡΓΩΝ ΠΡΟΚΛΗΣΕΩΝ
                print('12')
                player_data_main[winner-1].reset_wildcard_state()#ΕΛΕΓΧΟΣ ΚΑΙ ΡΕΣΕΤ ΣΤΟ ΜΠΑΛΑΝΤΕΡ
                
                player_data_main[loser-1].reset_wildcard_state()
                
                player_data_main[winner-1].alter_challenges_final_state()#ΑΛΛΑΓΗ ΤΗΣ ΚΑΤΑΣΤΑΣΗΣ ΕΝΕΡΓΩΝ ΠΡΟΚΛΗΣΕΩΝ
                
                player_data_main[loser-1].alter_challenges_final_state()
                
                ##############################################################
                del_classes(ch_valid_matches_main,(serial-1))#ΔΙΑΓΡΑΦΗ ΤΟΥ ΜΑΤΣ ΑΠΟ ΤΗΝ ΛΙΣΤΑ
                
                del_list(ch_valid_matches,heads_ch_valid_match,serial-1)
                
               ########################################################
                ########################################################
                SWAP(player_data_main,winner-1,loser-1)#ΑΛΛΑΓΗ ΘΕΣΕΩΝ ΠΑΙΚΤΩΝ ΣΤΗΝ ΚΑΤΑΤΑΞΗ ΜΕΣΩ ΤΗΣ ΧΡΗΣΗΣ ΤΗΣ ΚΑΤΑΛΛΗΛΗΣ ΣΥΝΑΡΤΗΣΗΣ
               #########################################################
                top = CONFIRMED(self)
                top.grab_set() 
            else:
                top = FAILED(self)
                top.grab_set()
                print('logic')
             
        except:
            top = FAILED(self)
            top.grab_set()
            print('except')

###ΚΛΑΣΗ ΥΠΟΜΕΝΟΥ ΔΙΑΧΕΙΡΙΣΗ ΕΚΡΕΜΜΩΝ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ###
class OUTSTANDING_CHALLENGE_MATCH(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Πρόγραμμα Κατάταξης Τέννις")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width//6}x{self.screen_height//6}+{self.screen_width//2}+{self.screen_height//2}")
        self.match = tkinter.IntVar()
        tkinter.Label(self,text="Αριθμός εκρεμούς μάτς κατάταξης",fg="black",font=("System",12,"bold")).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Entry(self,fg="black",font=("System",12,"bold"),textvariable=self.match).pack(anchor=tkinter.N,side=tkinter.TOP)
        tkinter.Button(self,height=1,width=10,text = "Επιστροφή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.destroy).pack(anchor=tkinter.SW,side=tkinter.LEFT)
        tkinter.Button(self,height=1,width=10,text = "Αποδοχή",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.confirm_match).pack(anchor=tkinter.SW,side=tkinter.RIGHT)
        tkinter.Button(self,height=1,width=10,text = "Απόρριψη",activebackground="white",activeforeground="red",bd=8,relief=tkinter.RAISED,fg="black",font=("System",12),highlightcolor="black",command=self.deny_match).pack(anchor=tkinter.SW,side=tkinter.RIGHT)
    ###ΑΠΟΔΟΧΗ ΕΚΡΕΜΜΟΥΣ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ###
    def confirm_match(self):
        try:
            number = self.match.get()
            if(number>=1 and number <=(len(ch_out_matches_main)+1)):
                
                taker_serial = ch_out_matches_main[number-1].taker_serial
                
                if(player_data_main[taker_serial].challenges_final_state==1):
                    
                ######################################################################
                    #ΕΑΝ Η ΜΕΤΑΒΛΗΤΗ ΠΟΥ ΕΙΣΗΓΑΓΕ Ο ΧΡΗΣΤΗΣ ΕΙΝΑΙ ΣΤΑ ΟΡΙΑ ΠΟΥ ΠΡΕΠΕΙ ΔΗΛΑΔΗ Ο ΠΑΙΚΤΗΣ ΜΠΟΡΕΙ ΝΑ ΑΠΟΔΕΚΤΕΙ ΠΡΟΚΛΗΣΗ
                    player_data_main[ch_out_matches_main[number-1].taker_serial].increase_challenges_final()   #ΑΛΛΑΞΕ ΚΑΤΑΣΤΑΣΗ ΕΝΕΡΓΩΝ ΠΡΟΚΛΗΣΕΩΝ ΣΤΟΝ ΠΑΙΚΤΗ ΠΟΥ ΤΗΝ ΑΠΟΔΕΚΤΗΚΕ
                    player_data_main[ch_out_matches_main[number-1].taker_serial].alter_challenges_final_state() #ΕΛΕΓΞΕ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΤΩΝ ΕΝΕΡΓΩΝ ΠΡΟΚΛΗΣΕΩΝ
                    add_valid_challenge_match(ch_out_matches_main[number-1].giver_serial,ch_out_matches_main[number-1].taker_serial) #ΓΡΑΨΕ ΤΗΝ ΠΡΟΚΛΗΣΗ ΣΤΗΝ ΛΙΣΤΑ  
                    del_classes(ch_out_matches_main,(number-1))# ΣΒΗΣΕ ΤΟ ΜΑΤΣ ΑΠΟ ΤΙΣ ΛΙΣΤΕς
                    del_list(ch_out_matches,heads_ch_out_match,(number-1)) #ΣΒΗNEI ΤΗΝ ΠΡΟΚΛΗΣΗ ΑΠΟ ΤΗΝ ΛΙΣΤΑ
                    
                ##################################################################
                   
                    pop_up = CONFIRMED(self)
                    pop_up.grab_set()
                else:
                    pop_up = FAILED(self)
                    pop_up.grab_set()
                    
            else:
                pop_up = FAILED(self)
                pop_up.grab_set()
                
        except:
                pop_up = FAILED(self)
                pop_up.grab_set()
                
    ###ΑΡΝΗΣΗ ΕΚΡΕΜΟΥΣ ΜΑΤΣ ΠΡΟΚΛΗΣΗΣ###
    def deny_match(self):
        try:
            number = self.match.get()
            if(number>=1 and number<=len(ch_out_matches_main+1)):
                del_classes(ch_out_matches_main,number-1) #ΣΒΗΝΕΙ ΤΟ ΑΠΟΡΡΙΦΘΕΝ ΜΑΤΣ ΑΠΟ ΤΗΝ ΛΙΣΤΑ
                del_list(ch_out_matches,heads_ch_out_match,(number-1))
                pop_up = CONFIRMED(self)
                pop_up.grab_set()
            else:
                pop_up = FAILED(self)
                pop_up.grab_set()
          
        except:
            pop_up = FAILED(self)
            pop_up.grab_set()
            
   
### MAIN###
if __name__ == '__main__': 
    root = MAIN()
    root.mainloop()   