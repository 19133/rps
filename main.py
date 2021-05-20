import random

# functions go here
def check_rounds():
  while True:
    response = input ("how many rounds: ")

    round_error = "Please type either <enter>"  "or an interger that is more than 0\n"

    # If infinite mode is not chosen, check response
    # is an integer that is more than 0
    if response != "":
      try:
        response = int(response)

        if response < 1:
          print (round_error)
          continue
          
      except ValueError:
        print(round_error)
        continue

    return response


def choice_checker (question):

  error = "Please chooosr rock / paper / scissors"

  valid = False
  while not valid:

    #ask the user for choice
    response = input(question).lower

    if response == "r" or response == "rock":
      return response

    if response == "s" or response == "scissor" or response == "scissors":
      return response
    if response == "p" or response == "paper":
      return response

    elif response == "xxx":
      return response
  





# Main routine

rounds_played = 0
choose_instruction = "Please choose rock (r), paper"  "(p) or scissors (s)"

user_choice = choice_checker("Choose rock / paper /" "scissors (r/p/s): ")

rounds = check_rounds()

end_game = "no"
while end_game == "no":

  print ()
  if rounds == "":
    heading = "continuous mode:" \ "Round {}".format(rounds_played + 1)
    
  else:  
    heading = "Round {} of " \ "{}".format(rounds_played + 1, rounds)

  print (heading)
  choose = input ()
    
    
    
  if choose == 'xxx':
    break

  else:
    heading = "Round {} or {}".format(rounds_played + 1, rounds)
    print(heading)
    choose = input(choose_instruction)
    if rounds_played == rounds -1:
      end_game = "yes"

  print ("you chose {}".format(choose))

  rounds_played += 1

print("thank you for playing")





