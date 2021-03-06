---
layout: post
title:  "enum trigger warning"
date:   2017-01-13 21:59:46.896400 -0800
categories:
---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"[Trigger warning](https://www.nytimes.com/2016/09/11/opinion/trigger-warnings-safe-spaces-and-free-speech-too.html)" may be another buzzword but a trigger can be a key unlocking something much greater. Let me tell you about an experience that taught me this.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(If you'd like to pass over the programming stuff, go ahead and skip the next paragraph)  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you've studied languages like C or Java, you've likely come across the `enum` ("enumerated") data type: (C was created during the Cold War, so an appropriate example shall follow)  

```
enum defcon_exercise_term
{
  COCKED_PISTOL,
  FAST_PACE,
  ROUND_HOUSE,
  DOUBLE_TAKE,
  FADE_OUT
} level;
```

Inside the curly braces we have some constants that are assigned to their index (starting at `0`) in the list that we can set the `level` variable to. (We need to add 1 to each value to get the real-life version. `COCKED_PISTOL` equals `0`, but we add 1 to get the correct value. `FAST_PACE` is `1` in the program, and so on.)  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I've hitherto never used an `enum` for a project, except one assignment for a high school class. I was typing away at my homework in the computer lab one uneventful day, and someone came up behind me, checked my monitor,  said something like "`enum`s? we didn't look at those until the end last year," and walked off. (He'd repeated the course, and we were only about halfway through the school year at the time.) Why do I recall such an everyday exchange? Probably it was one of my very few interactions with [the guy who went on to kill 3 people and injure one at a house party](http://komonews.com/news/local/3-dead-1-wounded-in-shooting-during-party-in-mukilteo) two years later.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I had a recollection of hearing about the incident and attending the proceeding vigil the first time I had to look at an `enum` in college, while grading Intro to Computer Science assignments just a few months after the incident. (I got to skip Intro freshman year and had not seen `enum`s since high school) I paused, reflected, and got back to work. The next time I encountered one was the other night, while I was studying basic C for my operating systems course, and I had the same recollection. A similar pause followed. That's when I realized something: `enum` had become something of a trigger to me, which was something I hadn't learned about until late last year. What happened the next day may have solidified it for life.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The following morning I read that the shooter had been [sentenced to life imprisonment](http://www.seattletimes.com/seattle-news/crime/allen-ivanov-to-get-life-in-prison-for-killing-3-classmates-at-mukilteo-party/) upon pleading guilty and apologizing to the families of the victims. The article was a hard read: I had seen images of the skulking inmate on trial, and others of victims' family members sobbing, but both in the same photograph was almost too much to handle. But while I may have an occasional trigger, other people have it much worse. My own occasional taste of it was an infinitesimal speck compared to the agony that others endure as a result of the man's actions.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In other cultures, people are given more space to mourn the loss of their loved ones: in Japan, family members are expected to grieve for one year upon the loss of a loved one, and receive visits from priests during that period. In America, we are known to give much less time. It's been said that time heals all wounds, and sure enough, I had seldom thought of the incident in the months that followed. But seeing the sentencing pop out of the everyday mix of news reminded me how much people are still grieving.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I can still clearly recall seeing the events unfold the weekend of the crisis. The initial reports of the shooting (at about 12:30 AM on July 30, 2016) only gave the street name and some blurry photos. That was only a couple blocks from where I lived from 1997 to 2012, which alone made the report pretty unnerving. When I learned the identity of the shooter, and that it had taken place at my old friend's house, I was in shock. I got that message while driving from Poulsbo (my current residence) to Ballard to attend a Magic: The Gathering tournament, which I still attended but I couldn't focus and quickly dropped out. I haven't picked up the game since then. (Perhaps I'm subconsciously avoiding picking up other triggers?)  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Feeling sick to my stomach I drove home. The next day, I attended the LDS church parking lot vigil in Mukilteo, just a 2-minute trip from my old neighborhood where it all took place. It had the combined atmosphere of a high school reunion and a memorial service: many a recognizable face, all solemnly turned downward. Old memories took on new form as a looming specter. After sitting through a few pompous religious speeches (to a largely non-religious crowd) I happened upon one of the survivors of the attack. I had not seen him in years after a falling-out of sorts, but we embraced and shared good company for a moment. Afterwards I ran into one of my old math teachers, who seemed happy to learn that I'd chosen a mathematics major despite having slacked off in his precalculus class, and after a pleasant conversation I headed home and continued life as it were in Poulsbo.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I regret that I have nothing to say of the deceased; I did not know any of them personally. Times like these remind us of how fragile and dependent we are on others for our own well-being, regardless of what we think of them at any given time. The two interactions I had at the vigil with people I may had otherwise wanted to forget about made negative triggers a little positive. I had the conscious obligation to attend, but those interactions that followed permeated my subconscious to the extent that I can acutely recall them months later. We were all  battling inner demons for certain, and that seemed to be true of everyone. It was at that moment that I learned the important value of sympathy, whether I realized it or not.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It came in handy when I took a lab assistant job for an Intro to CS course at my university. I was a bit nervous going into it at first, but it turned out to be one of the greatest parts of the semester. I looked forward to it every week even. Not because of the code: it was all stuff I was already familiar with having studied it years prior. But getting to help others solve problems was the best part of it. We were all connected somehow: they needed me to answer their questions, and I had returned a better experienced programmer from having explained the introductory concepts. I worked overtime to help students and collaborate with the prof over email to make sure all the class members were alright. It just felt right.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We have a moral prerogative to help one another. We are all gifted, and we must share our gifts with each other. We are interconnected due to, among other things, our shared need of emotional support. It's impossible to know what everyone's triggers are, but offering a helping hand at what we're good at when it's needed is always appreciated. Everyday actions make a huge difference. These can activate positive triggers--responses to genuine kindness--we all share. But simple, small things need to happen for this reaction to occur. Without these actions, we may end up losing each other.  


Dedicated to Anna, Jordan, Jake, and Will
