"""
Author: Linda MEGNE
Email: lindamegne@gmail.com
Slidell, 07/10/2015
"""

import itertools

BANNER = "-" * 60


class output_print():
    """
        Print words counted, the number of time they appear in a text file and on screen
        Print median updated as tweet messages come in  in a text file and on screen
        
    """
    def __init__(self):
        """
            Function: init 
            --------------
            
            Initialize global parameter
        """
        self.my_list = []
        self.my_dict = {}
    
    def print_med_to_screen(self,med_list):
        
        """
            Function: print_med_to_screen
            -----------------------------
            
            med_list: median calculated as tweet messages come in
            
            The function design a nice print out to screen
            
        """
        m_list = med_list
        print("[Number total of tweets: %d]" % len(m_list)).center(60,"=")
        print("median numbers list updated")
        print BANNER
        for w in m_list:
            print(w)
    
    def print_med_to_file(self,  med_list, file_name):
        
        """
            Function: print_med_to_screen
            -----------------------------
            
            med_list: median calculated as tweet messages come in
            
            The function design a nice print out to screen
            
        """
        m_list = med_list
        file_object = open(file_name,"w")
        file_object.write(("[Number total of tweets: %d]" % len(m_list)).center(60,"="))
        file_object.write("\n median numbers list updated\n")
        file_object.write(BANNER + "\n")
        for w in m_list:
            file_object.write("% 0s\n" % w)
        file_object.close()
        
    def print_words_to_screen(self,words_dict, is_reverse = False):
        
        """
            Function: print_words_to_screen
            -----------------------------
            
            words_dict: dictionary of words and their frequency
            file_name: out put text file
            
            The function design a nice print out of the list of the words
            and their frequency to the screen.
            
        """
        words = words_dict.items()
        words.sort(key = lambda(a,b):(a,b), reverse = is_reverse)
        print("[Words tweeted: %d]" % len(words)).center(60,"=")
        print("%-25s | %25s" % ("Words", "count"))
        print BANNER
        for w, c in words:
            print("%-25s | %25d" % (w, c))
    
    def print_words_to_file(self, words_dict, file_name, is_reverse = False):
        
        """
            Function: print_words_to_screen
            -----------------------------
            
            words_dict: dictionary of words and their frequency
            file_name: out put text file
            
           the function design a nice print of the list of the words
           and their frequency to file.
            
        """
        words = words_dict.items()
        words.sort(key = lambda(a,b):(a,b), reverse = is_reverse)
        file_object = open(file_name,"w")
        file_object.write(("[Words tweeted: %d]" % len(words)).center(60,"="))
        file_object.write("\n%-25s | %25s\n" % ("Words", "count"))
        file_object.write(BANNER+"\n")
        for w, c in words:
            file_object.write("%-25s | %25d\n" % (w, c))
        file_object.close()
