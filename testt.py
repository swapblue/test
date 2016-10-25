import random
import itertools
def team_select():
"please select two teams"
team_one = raw_input ("please select name of first Team >> ")
team_two = raw_input ("please select name of second team >> ")
print "\n"
print "so today's match is between %r and %r " %(team_one,team_two)
fun_toss(team_one,team_two)
#batting(coin)
def fun_toss(team_one,team_two):
print "we are here for toss \n"
print "its %r teams call..... \n" %team_one
toss_optn = raw_input ("please select heads or tails >>> ")
coin = random.randint(1,2)
if coin == 1:
print("Heads!\n")
print "congratulations... %r won the toss" %team_one
elif coin == 2:
print ("Tails ! \n")
print "congratulations ... %r won the tosss" % team_two
batting(coin,team_one,team_two)
def batting(coin,team_one,team_two):
total_run_team_one = 0
total_run_team_two = 0
if coin == 1 :
print "%r team comming for batting " %team_one
for batsman in range (1,3):
batsman_name = raw_input("next batsman name >> ")
batsman_run =int(raw_input("run scored >> "))
print "%r scored %r run's : " %(batsman_name,batsman_run)
total_run_team_one = (total_run_team_one + batsman_run)
print "Inning comes to an end ..... ! so the total run scored by %r is %r" %(team_one,total_run_team_one)
print "\nSecond Inning Started"
for batsman in range (1,3):
batsman_name = raw_input("next batsman name >> ")
batsman_run = int(raw_input("run scored >> "))
print "%r scored %r : " %(batsman_name,batsman_run)
total_run_team_two = (total_run_team_two + batsman_run)
print "Inning comes to an end...... ! so the total run scored by %r is %r" %(team_two,total_run_team_two)
winning_team(total_run_team_one,total_run_team_two,team_one,team_two)
elif coin == 2:
print "%r team comming for batting " %team_two
for batsman in range (1,3):
batsman_name = raw_input("next batsman name >> ")
batsman_run = int(raw_input("run scored >> "))
print "%r scored %r : " %(batsman_name,batsman_run)
total_run_team_two = (total_run_team_two + batsman_run)
print "Inning comes to an end...... ! so the total run scored by %r is %r" %(team_two,total_run_team_two)
print "Second Inning Started"
for batsman in range (1,3):
batsman_name = raw_input("next batsman name >> ")
batsman_run = int(raw_input("run scored >> "))
print "%r scored %r run's : " %(batsman_name,batsman_run)
total_run_team_one = (total_run_team_one + batsman_run)
print "Inning comes to an end ..... ! so the total run scored by %r is %r" %(team_one,total_run_team_one)
winning_team(total_run_team_one,total_run_team_two,team_one,team_two)
def winning_team(total_run_team_one,total_run_team_two,team_one,team_two):
if total_run_team_one > total_run_team_two:
print "\ncongratulation %r team won the match.." %team_one
elif total_run_team_two < total_run_team_one:
print "\ncongratulation %r team won the match.." %team_two
elif total_run_team_two == total_run_team_one:
print "\nmatch is draw"
team_select()
