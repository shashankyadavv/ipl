import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\HP\Downloads\ipl_2022.csv")
print(data.head())


# import os
# print(os.getcwd())
# The dataset contains all the information needed to summarize the story of IPL 2022 so far. So let’s start by looking at the number of matches won by each team in IPL 2022:

figure = px.bar(data, x=data["match_winner"],title="Number of Matches Won in IPL 2022")
figure.show()


# So, currently, Gujrat is leading the tournament by winning eight matches. It is an achievement as a new team for Gujrat in IPL. Now let’s see how most of the teams win. Here we will analyze whether most of the teams win by defending (batting first) or chasing (batting second):

data["won_by"] = data["won_by"].map({"Wickets": "Chasing", 
                                     "Runs": "Defending"})
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold','lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Defending Or Chasing')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()





# So, currently, 24 matches are won while chasing the target, and 22 matches are won while defending the target. Now let’s see what most teams prefer (batting or fielding) after winning the toss:

toss = data["toss_decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue','yellow']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision')
fig.update_traces(hoverinfo='label+percent', 
                  textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()







# Thus, most captains choose to field after winning the toss. So far, in 43 games, captains have chosen to field first, and in just three games, the captains have chosen to bat first. Now let’s see the top scorers of most IPL 2022 matches:

figure = px.bar(data, x=data["top_scorer"],
            title="Top Scorers in IPL 2022")
figure.show()

# Currently, Jos Buttler has been a top scorer in 5 matches. He is looking in great touch. Let’s analyze it deeply by including the runs scored by the top scorers:

figure = px.bar(data, x=data["top_scorer"], 
                y = data["highscore"], 
                color = data["highscore"],
            title="Top Scorers in IPL 2022")
figure.show()





# So till now, Jos Buttler has scored three centuries, and KL Rahul has scored two centuries. Now let’s have a look at the most player of the match awards till now in IPL 2022:


figure = px.bar(data, x = data["player_of_the_match"], 
                title="Most Player of the Match Awards")
figure.show()


# So Kuldeep Yadav is leading in the list of players of the match awards with four matches. It is a great tournament for Kuldeep Yadav this year. Now let’s have a look at the bowlers with the best bowling figures in most of the matches:

figure = px.bar(data, x=data["best_bowling"],
            title="Best Bowlers in IPL 2022")
figure.show()

# You can see Yuzvendra Chahal having the best bowling figures in four matches. So this is a great tournament for Yuzvendra Chahal this year too.

# Now let’s have a look at whether most of the wickets fall while setting the target or while chasing the target:

figure = go.Figure()
figure.add_trace(go.Bar(
    x=data["venue"],
    y=data["first_ings_wkts"],
    name='First Innings Wickets',
    marker_color='gold'
))
figure.add_trace(go.Bar(
    x=data["venue"],
    y=data["second_ings_wkts"],
    name='Second Innings Wickets',
    marker_color='lightgreen'
))
figure.update_layout(barmode='group', xaxis_tickangle=-45)
figure.show()

