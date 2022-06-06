{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def turn_right():\
    turn_left()\
    turn_left()\
    turn_left()\
\
# get in a position where there is a wall to the right\
while front_is_clear():\
    move()\
turn_left()\
\
while not at_goal():\
    if right_is_clear():\
        turn_right()\
        move()\
    elif front_is_clear():\
        move()\
    else:\
        turn_left()}