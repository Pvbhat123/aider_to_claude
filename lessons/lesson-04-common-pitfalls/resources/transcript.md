Welcome to Lesson four of principled AI coding.
Now that you have a great grasp on AI coding, We're leaving the fundamentals and entering the intermediate zone.
In this lesson we're going to look at how AI coding goes wrong so that you can resolve these common issues
As we've touched on, AI coding is about hitting the big three Bull's Eye not just once but throughout your AI coding sessions.
That means when your AI coding tool has hallucinated or caused an issue, one of your three elements is likely off and needs to be addressed.
This lesson is about fine tuning your scope so that you can become an AI coding sniper and always hit the Big Three bull's eye by avoiding common pitfalls that chew up your performance time and engineering output.
After we discuss pitfalls and their solutions will focus on boosting your capabilities over the long-term by digging into new aspects of your AI coding assistant.
Let's turn our attention to the principle for this lesson balance, then boost first, do it, then do it right, then make it fast
In lessons one through three we learn how to do it in this lesson we focus on doing it right when you are coding with AI you first want to align your big three bulls eye by balancing your prompt context and model then it's all about boosting your capabilities by mastering your AI tooling and pushing it to its limits.
Let's break down common pitfalls for AI coding as well as their solutions.
These are issues you're going to see again and again, even with next generation language models and great AI tools, but after this lesson you'll know exactly how to fix them as soon as they happen and you'll know how to prevent them from happening in the first place so to get started, let's go ahead and open up our terminal and every time ELs you can see our previous three lessons.
Let's go ahead and clone in The lesson for Rebo Link is going to be in your loop Boox I'll type Get, clone drop in the lesson for code base, If we type
Ls you can see we have the fourth lesson there, so go ahead and seed into this then I'll open vs code here be sure to paste in your lesson three is.environment file Here let's open our main file and we'll go ahead and collapse so that we can see what we have here so from the file explorer and from our main file You can see we have a slightly modified version of our lesson three code base we're going to use it as a playground to showcase common pitfalls in AI coding Let's open up the read me inside of this file you'll have the set of instructions and you'll also see a concise list of the common pitfalls that we're going to work through today across the context model and the prompt will go ahead and collapse these so we can focus on them one at a time.
Let's start with the context.
This is the first place things go wrong with AI coding.
There are two main varieties of context pitfalls You're either missing context or you have too much context.
Let's start with missing context.
Missing context is one of the easiest and one of the most common AI coding pitfalls.
Let's run this setup command and then we'll execute this prompt.
To see this in action I'll open up a terminal and let's copy the setup command PAS in the terminal.
This is a new syntax that you can use to start AER with files in the Context window.
So we enter here
Aa will automatically boot up with these files and our context window.
You can see those two here when we review our code.
Here we can pull on the main.
We can also command Click to open our Main and command click to open our output format right from the A or chat window and let's go ahead and set up our prompt add a new output format Tamil, so we have a kind of simple, High Level prompt and as we saw in lesson three we are missing a file.
What file is missing?
If we open up our file Explorer, we can see that our parse is missing.
If you remember we have this parse arguments function that is pulled in from our arg parse file in our context window.
Here that file is completely missing.
We're going to be executing this, we are missing our Arg parse file, and this is one of the most common issues that happens.
You're just missing context, so you run a prompt and some details get missed.
If we just look at the E or output, we can see exactly what happened.
We did successfully add the format function in our main file.
We add the import properly, we got the output format here and we added Tamil, which will help us parse Tamil, but we did not update our parse.
This is a very simple, very straightforward issue.
We'll skip running this command as we know the solution here is very simple.
Add the files.
This is not ultra useful advice.
The principled way to solve this problem across time is to always think from your AI coding assistant perspective, Always know what your AI coding tool can see here is a great practice right before you send your prompt think would I be able to solve this problem with these files and this prompt this small practice can save you from the missing context pitfall A coding tools will progress and they will improve the ability to pick up on missing context Obviously we're just working with three files on a small code base, so it's not a huge issue, but missing context files becomes a big issue when you miss 12 or five plus files that need to be edited in a large context, Prompt when you're running a prompt against ten plus files having the updates misaligned after your prompt runs can be time expensive to fix every mistake we make cost something for engineering work, it's usually time and resources The cost of this mistake is low to medium severity based on how many files you've missed we can use Aiders Undo command to revert the previous change that was just made so you can see that we've just undone our Tamal change and now we can add our hard parse file, so this is the normal way to fix this, but I want to show you a great feature in AER and another reason to use low level prompts, AdR will automatically suggest adding a file if we explicitly mention it in the prompt.
Let's clear out the chat so that we know AER is not cheating with the file history and then let's run this update source and then we'll just look for that art parse file and then we'll say comma start up PY
So this is just us adding a little bit more detail we're saying make sure that you also update every other file and then we'll say add a new output format Taml and you know, just to be super clear and blunt about it, you can see we did remove all of our previous Taml code.
Right, that's no longer an output format.
Now let's go ahead and run this prompt with a reference to the file we want to add in the prompt will hit Enter and you can see right away a or is asking us Hey, you mention this file but it's not in the chat do you want to add it?
Well of course it yes and now before this prop executes a is going to add it to the context window and so now you can see that change coming through across 123 files you can see that change added here in our Arg parts it imported the file, we got the output format change and we have the updates in the main file we have a little linting issue we can hit yes, and it will automatically fix that for us at As AI Coding Tools Progress Context Management will improve, but fundamentally there will always be some process where we tell the assistant what we need changed or some mechanism where it guesses and then we confirm not thinking about what your AI coding assistant can see is an easy mistake to make and among the most common we'll go ahead and clear and let's go ahead undo our change Since we're just using this code base as a way to showcase common pitfalls and solutions to go ahead and undo and let's go ahead and run it again to fully remove the tumble change.
Now let's go ahead and look at the inverse issue excessive context, so let's clear hop back to our read me and let's look at the setup for excess context.
The larger the context window, The more your coding assistant and the underlying large language model has to make decisions about where things need to go.
Your low level prompts with locations, actions and details reduce the chances that this will happen, but in large code bases with similarly named variables, functions, classes, files and directory names.
It's just as confusing for a large language model as it is for engineers.
Even great models will make mistakes when working with code that is hard to distinguish.
Even great engineers make mistakes in an overloaded context situation where there are too many files at play, an overloaded context is essentially too much information at once you can imagine the model becomes overwhelmed and confused, causing it to predict a bad next token and therefore cause issues as you know with even just one line off or one syntax error Your entire program is cooked.
It's incredible when you think about it, how precise we as engineers need to be on a daily basis.
Thankfully, these AI tools can help us be more precise and faster than ever.
If we know how to use them properly to test this, we can run this massive AER startup command and we can paste this and here and what this will do is use these two glove patterns to add multiple files to a code base at once, so if we open up our file Explorer
This first glob pattern will add everything in our root directory and this second glob pattern will recursively add every Python file from every directory so we can kick this off and now you can see we have a ton of files in our context window, It's important to note that Glob patterns and AER file adding in general will only add files that are not ignored by via your.get Ignore file
This is really important it's only adding files that it can see through get so if we scroll up we'll see something kind of interesting and important warning it's best to only add files that need changes to the chat AER is, you know, explicitly calling us out already, your context is going to get overloaded your language model is going to have issues guys so right away we're getting a warning for that I like that that's built right into a or even AER gave US-A warning that we are walking into dark territory.
Things are going to go wrong with this much information in our context window we can type Slash tokens to see where the distribution of all of our tokens are coming from across our context window you can see here there are some obviously large offenders.
We have our UV lock file costing about $0.08 of prompt bunch of things that don't need to be in here.
This is just an example of sloppy context management.
Let's go ahead and run our prompt against this context management and let's see what happens.
So we have this prom update the analyze transcripts V to function to include additional logging and sentiment analysis and the next type version.
So there's a couple things going on here you can see this also isn't the best prompt BO talk about prompts more in just a moment.
Let's go ahead and paste this and and let me just show you a little bit of what we have here so if I just click on our transcript analysis you can see here I have a couple additional transcript related messages these are kind of just mock methods, but you'll notice that you know, we have a lot of similarly named methods here where we have analyzed transcript,
We have analyzed transcript with logging Analyze transcript V two and then if we open up our data types you can see we have a couple of types that are named in a very similar way in large production code bases you're almost guaranteed to get code and files that are named nearly exactly with some small variations right like here we have the two we have the next you can imagine there are, you know, sub types of transcript analysis maybe have some enums or some other types.
This happens especially when you're centralizing around a specific domain problem, so let's go ahead and just run this prompt and let's see what happens so we'll go and just kick this off and you know we have a huge context window here, there's a lot going on we have you know a couple methods here that are going to replicate us being in a large production code base and you can see our a coding assistant is making its best guess at what to do here.
It's trying to match against this V two analysis function, it's adding some logging, it's returning this next, you know the next type frankly, all in all, it's doing a pretty good job at just kind of guessing at which one of these methods we actually wanted and which one of these, you know types we were looking for also pouring to call out we just torched $0.15 by overloading our contact window So not only is a large context window confusing for the LM we force it to guess be forced to make decisions.
We're also just torching cash.
We don't have to look through the changes.
I'm going to assume that the LM made its best guess based on the prompt and the context window.
All things considered are A coding assistant is doing a good job here.
If we got back to our read me, It's important to note that a lower level prompt can compensate for you having an overloaded context window.
Right, there's always this idea of intersecting your big three elements you can compensate when you are not managing your context properly, you can write a great accurate, low level a quoting prompt and it will shift through all the noise that you've provided it, but the long-term principle based solution.
Here is the same as having missing context.
Always think from your AI Coding Assistants Perspective Could you solve the issue with the prompt and the context you're ready to launch, if not change it in the case of an overloaded context, It's a medium severity issue because if your AI coding assistant guesses wrong and starts updating the wrong files you now have to update those files as well as make the change that you actually wanted Now let's talk about common issues with the AI coding, prompt common pitfalls with a prompt come down to two issues your prompt is either too High Level or it's too low level, Let's focus on the first case because it's the most common let's clear out our chat window here and boot up AER with only our Python files you can see here using the glob pattern and we're being better about our context window we're only adding Python files now, so they'll all be code relevant and now we have all these items in our chat and then we have this prompt enhance the visualization of our data top and bottom so this is one of the most common issues in effect, a High Level prompt as we touched on is a prompt that is focused much more on the what and less focus on the how prompts that are too High Level are over focused on what to do, void of detail on how to do it, although the tides are and will continue to shift toward the what and High Level prompts we still need to include enough detail so that our AI coding Assistant and the underlying language model know how to get the job done.
There's a sweet spa you ought to be aiming for mid level prompts.
There is a mid level prompt that we want to strive toward with every E coding prompt that we write.
Sometimes the mid level is closer to the High Level, sometimes is closer to the low level with more details.
This is how prompt phrase structures we discussed in lesson three can be really useful.
The location, the action and the detail really help drive accurate, consistent results from your large language model.
Let's look at this prompt that is too High Level and does not have enough detail to get the job done right, enhance the visualization of our data top and bottom so let's close a few files here and let's look at our main file, so this version of the application has three visualizations we now have a bar chart, pie chart and a line chart if we open up our chart up PY you can see these methods here simple enough right so we actually have three visualizations now and if we were to run a prompt like this with your experience already from the first three lessons you can already see massive issues with this right enhance the visualization.
Okay, that's vague.
Right what visualization of data data is just a terrible terrible word in general there's very little information here.
This is one of the words that should just be banned from engineering unless it's in some type of context and then we say top and bottom so what is top and bottom maybe the highest count, the lowest count our language model has to guess here right, it's making many guesses about what we actually want to do here, let's go ahead and just fire this off and let's see what are a coding assistant comes up with here let's see what the Ln comes up with will this fire this off here, you know, language models are progressing, they're improving a lot so it's going to come up with something here, but right away you can see we're updating all of our visualizations, so it's firing off on all three prompts we didn't say what So it's tweaking some of the labels, it's adding some text to some of our points, It's doing a little bit of work on the title of the pie chart and it's adding some annotations for our chart up PY Right so it's it's just too High Level like what are we actually asking for here again thinking from our er coding systems perspective enhance the visualization like imagine if a Product Manager asks you to do this What does this mean?
Enhance the visualization of our data top and bottom Okay so you know I chose and kind of wrote a particularly vague and bad High Level prompt, but you get the idea and I can imagine you have run prompts like this yourself, maybe just testing something, maybe just doing things AD, HOC, but you can see the point.
This is a prompt that's too High Level is void of useful information that helps drive results so we can go ahead and just kick off our application and we can actually just see what our language model changed here, so if I just copy this command here, let's go and run our transcript application with Minl 15 we'll have three visualizations pop up here first our bar, then our pie and then our final chart so we can see we have some you know, a little bit of additional information here it didn't get what we wanted, you know, we can look through the rest of our items here we have this nice frequency pie chart and then a line trend Okay, so let's improve this prompt with ID cases and let's make it rich in location, action and detail prompt phrases a pattern you can consider for writing concise a coding prompts especially the larger ones I recommend you just open a file, open up the contacts where I just have your terminal open here you can see the context and then just work on an empty file so we can start by saying Update chart up PY and let me go ahead and run Slash Ondu to revert the changes here, so we're back at our original state, No changes to our visualizations and we can go and run clear as well.
Word count bar chart so here we're using a function information dense keyword and then I'll just go ahead and add the nesting here in the statement, so I'll say update the top quartile of data to be green comma so we have a list of changes, a list of details that we want then I'll say The Bottom quartile red, the remaining blue you can see here this prompt is much more detailed without even adding that many more tokens words characters.
Right let's go and just copy those and let's just look at these side by side.
Right, look at how much information this has we are now telling our LM Hey, we only need updates to this one file, regardless of how many files are in your contacts window they update this one file, Update this function and here are the changes I want you to make top quartile of the data green bottom red, remaining blue and of course, the language model knows what a core tile is we have two information dense keywords here, every using our clear, concise update keyword here and then we have our file keyword and our function keyword so there's no confusion here.
Right, I invite this prompt and I know exactly, I don't know the exact lines.
Right, I don't know how the Elm will do it, but I know what it's going to do with zero confusion so you can see there it's creating the COR tiles, It's worth the change it updated only that function and only the chart file and we can go in and just kick this off again drop our mean come threshold will switch that to ten and now before even seeing the output, I know what the output here is going to be right, we have the top quartile red The Bottom quartile green and the remaining blue just very simple, very straightforward, we can be very confident in our changes.
Why, because we left no room for confusion, we wrote a low level, prompt, rich and information, dense keywords and prompt phrases
When you follow structure, When you follow patterns you get repeatable results.
That's a lot of what we're doing in this course.
We're trying to win not just today, not on this one, prompt, not with this one tool were aiming to set ourselves up with principal based approaches and patterns that we can reuse across a coding tools across time in terms of the severity and the cost of writing a High Level prompt like this definitely can be fairly large.
I would put this at mid, severity, maybe mid to heavy severity.
It's almost guaranteed that you'll need to follow up and write at least one additional coding prompt with more detail.
Why not just skip all that in your first prompt?
Right, just write a great low level prom to begin with, low level props enable you to write perfect props for your A coding assistant.
It's going to be able to digest and then start working for you with no issues.
If it does by chance hallucinate, let's say our assistant hallucinated with this somehow there's really not a lot you can do.
Right you've pushed it to the limit, you've given it everything it needs, you've done your job just like working with a co-worker, you can't know what they're going to do with 100% certainty you can get close right as you build up that trust, just like we're building up our trust with these large language models and with our AI coding assistant writing low level prompts is a great habit that prevents issues from arriving when you're AI coding in real production applications with hundreds and thousands of files with a large ten plus file context Window and with real requirements, you want to use low level prompts to be precise and to avoid spending more time writing, more prompts now let's go ahead and look at the inverse case of this, let's take this exact same prompt and pop it to a read me so let me just copy this out.
Let's copy this, look at the read me and the prompt is too low level so we're going to do the same thing here.
Let's go ahead and revert this change so again just/undo and you know we can clear, do a full reset here these are basically the same file, so it's not a huge deal.
Let's go ahead and take this prompt and solve the opposite issue.
Your prompt is too low level. I'll admit this is a super low cost pitfall and few engineers, few AI coders are actually going to be making this issue of writing a prompt that's too detailed.
Some of us are super detail oriented.
Maybe that's you, maybe you fall into this camp.
Let me change the follow load here, but very few of us are going to be writing super high-quality prompts and wasting too much time.
This is the end of the spectrum you want to be on, especially when you're starting, and especially as you're pushing your E coding tool to do more for you, low level prompts are a great place to start and they're a great place to return to as you find yourself writing higher level prompts which are by design void of detail, Right, so at some point you're going to make a mistake writing a High Level, prompt moving fast that's bound to happen when it does move to a low level prompt, but you know when you have a low level prompt like this we can resolve this by practicing and just by being more concise with the prompt so let's try to rewrite this prompt to the sweet spot, right, this prompt is in fact a little too low level we can condense it even further.
Let's try to get to that mid level, right, so we can rewrite this prompt by saying the following update and let me just quickly turn the co-pilot off.
Correct word count bar chart make top quartile green, bottom red, rest blue got same thing let's do a token check this is 16 tokens and above we have 33 tokens, so till nearly a 2X improvement in total tokens, roughly total time to write and we can go ahead, kick this off just as before.
Right, make sure that everything's all clear.
No history we can kick this off right, so this mid level prompt is going to do basically the exact same thing.
Right it got the exact same work done, we can see it right here search replace you know, another shot up to AER as an a coding tool, it's very visual, it shows you what it's doing, The observability is fantastic, but you can see here we got that replacement just as we asked, We can go ahead once again, hit up, we can kick this off again and same result.
This is the important thing to call out with a coding tools we have the same result in half the prompt, right, we cut the prompt in half we got the same results.
How why we use information dense keywords like update and make to steer the actions of our prompt phrase, and then we use the function Information Dense keyword to specify a location, so this is very important, right within our context there is only one word count bar chart we can see that and our AI coding assistant can see that so there is no confusion about where this update should go Our Aing assistant either has to find the spot or has to blatantly hallucinate and that's exactly what you want, you don't want any fault to fall on your prompt and then we added our details.
Right are simple list details again.
Lots of information here packed in.
We're using the lists and we're allowing our LM to infer the pattern we want top quartile green, bottom COR tile red.
Right, that's hidden information here, this is embedded information using commas so it's a continuation and then the rest blue this prompt is nearly perfect.
We might be pushing a little bit to the High Level here.
You could imagine the quartile information may be getting missed using this rest pattern, but unlikely and you know, these are the prompts that I recommend you try to aim for.
This is kind of a gold standard, but the cost of writing a prompt that's too low level like this is just much lower, Right, because because what's the worst thing that happens?
You spend a little bit of extra time say say a minute writing a great prompt phrase, information keyword dense prompt that does the job perfectly and you know, that's pretty great out of all the common pitfalls
This is the least offensive one, not much more to say here, let's move on to common pitfalls surrounding the model, so language model issues and pitfalls are simple to see and simple to solve.
The biggest pitfall is usually using a weak and cheap model.
This is a huge mistake.
I see a lot of beginners make and the serious cash savers make and we can easily showcase this.
Let's go ahead and run Slash Undo let's actually just clear out this ater instance and let's run this command another cool feature and AER you can run a or from the command line and kick it off with a specific model, so of course we're going to use DP for O many as our weak cheap model, it's a fantastic model, but when you're writing code when you're trying to save time,
This is not the model to choose.
Let me show you why we're going to add all of our Python files once again and we're going to run this prompt that we did before.
Right, add a new output format Tamil Right and remember we reverted our Tamil chain SE if I search all throughout the code base, you can see it's only here in the read me close this and let's just kick this off Right, let's see what this weak model does, Right, so we'll just go and kick this off it has all the context it needs to solve this problem, but it doesn't have the juice right, it doesn't have the intelligence to even in this small code base, Look at everything, digest the context, digest the prompt and actually make the change we need, you can see it missed our arc parse file and it's just kind of hard to miss.
Right, it is, this is a hard thing to miss.
We have our parse arguments function here right at the top which contains our output format that we kind of need, right, so our small model miss this you know you might be thinking can't you write a lower level prompt to give Gbt for o many more guidance on how to solve the problem.
Yes, you absolutely can.
Low level prompts and context trimming will give for Oh, many a better chance, but weak models have limits.
The only question is, where is it When you use a higher tier model like Sonic 3.5, it will be immediately clear that using cheap models force you to do more work managing your context Writing lower level prompts, which will ultimately burn up more of your time.
This does not scale well into larger code bases.
You saw it here with only what eleven files in our context, it made a mistake with just eleven files.
I completely understand the desire to save money, not overspend and to use the cheapest tool that can get the job done.
This is smart thinking Where it stops Being smart thinking is when you don't include the value of your time and the experience you'll gain by using the best model at the right price.
Forgive me if I sound a little harsh here, but if you fall into the cheapest model, shortest, prompt, smallest context in an effort to minimize costs, you're not thinking long-term enough and you're not getting your reps and for when the models inevitably do become cheaper and you're able to use powerful models to get a lot done, you won't know how to utilize them properly every a coding prompt You run improves your experience with a coding tools every a coding prompt you run saves you time because you're offloading the code generation to your coding assistant and the LLM.
These models will continue to get cheaper and they will continue to improve.
Right now, it's vital that you focus on getting things done and understanding the capabilities of great base models.
Don't waste your time writing super low level prompts and paying too much attention to trimming your context window at the cost of going cheap, right when you're using Sonnet or GPT for O or a really solid near state of the art language model, that's when you want to trim your context, that's when you want to use proper low mid level prompts but you don't want to do that because you're trying to cheap out on this stuff.
There are hundreds of situations where I could have saved money doing things a cheap way, but the loss would be tremendous.
We can never get our time back.
This is the most valuable resource this lesson and this course is meant to help you save time, so don't cripple yourself by going super cheap when you have the option to use a legit powerful model I would not have been able to push my abilities if I was using cheap models and I would not have been able to create this course or get even a quarter of all the work done that I have with these incredible tools, Great engineering is about making tradeoffs and prioritizing speed, cost performance Pick two I highly recommend you optimize for speed and performance in the generative AI age with your AI coding assistance, Every property right is an investment in your time,
This is what great technology does you invest in it and it gives you back more value while consuming less every time.
Let's move on.
The inverse of this, of course, is model overkill.
As an exact example we can undo these changes, go and just clear rerun air and here you can see we're booting up with the you know, one of these state of the art models at the time of filming this model for many of the problems.
Frankly, nearly every problem that you could throw at this small code base is likely overkill, so you know we can paste this prompt and using our powerful oh one reasoning model and we can run this you know, it's basically that same mid level prompt update Word Count Star and this will update all of our word count visualization so not just a bar chart, but all three were using this kind of glob syntax pattern that language models know really well so it knows that we want to update all three of these we can enter really.
There's nothing wrong with this.
The severity of running a prompt like this is low to mid, but as you can see, this is taking some time and I'll likely have to cut this part out of the video.
I don't want to just waste time.
There you go.
We finally got a response.
The most obvious thing is just to not overkill.
This is a really Simple One.
It's unlikely you're going to make this mistake, but it's important to call out because it finishes the picture on balancing the big three bulls eye.
Right, you don't want too much or too little of anything you don't want to overkill with a very powerful model, like a reasoning model When you're doing small problems that don't need the power, they don't need the speed and frankly, they don't need you to cook your wallet like this prompt just it for me.
Right, so in the next lesson we're going to be using these powerful reasoning models the right way, really pushing the amount of code and the amount of reasoning and the amount of problem solving that they provide us, we're going to be focusing on that in our next lesson so stay tuned for that and I hope you can see the big theme of every one of these common pitfalls we've discussed right with the prompt, with the context and with the model it's either too little or too much, right, too little, too much, too little, too much.
This is why this is a balancing game.
Our principle here is balance then boost Okay, so we've covered many pitfalls you're likely to run into while AI coding at scale at an intermediate level, most are coding in this range in the zone is about avoiding too little and too much across your context model and prompt or balancing the intersection of the Big Three.
Now, after you've balanced your context model and prompt, you can start boosting your
A coding by going bigger.
As we've mentioned in our next lesson, we're going to push into using reasoning models and an agentic pattern for dual model coding.
AER has an entire mode around this called architect.
We'll get into that in the next lesson, but even before we get there, There are many things we can do to boost our productivity with a coding tools.
I want to laser focus in on AER as a base level AI coding tool, and break down how you can get more out of it.
It can be easy to start using tools like AER, get a ton of value out of the core features and miss out on going deeper.
I chose AER for this course for many reasons.
Open source terminal base unbiase control great research behind it great experimentation behind it and also due to the fact that it's customizable to the core.
Digging into your AD tooling beyond the surface will help you get everything you can out of your tool Since using either.
And Since it's foundational AI coding software, Let's look through a few lesser known features this tool has that can give you a great idea of what a comprehensive AI coding tool can offer.
Remember this course and AI coding is not about a single tool.
A coding is a skill that you can transfer to any tool, especially with the guiding principles we're covering in this lesson and in this course AER is the best tool to start with because it is a foundational tool that simple, open source yet highly configurable, it's a tool that current and future AI coding will intersect mirror and straight up copy.
It's funny to think most engineers won't know that AER was one of if the not first tool to have multi file editing.
Guess who everyone looked to to understand how to build this feature AER everything seems so obvious after it's been done right, I hope this course is starting to feel that way for you obvious natural focusing on the context model, prompt using powerful information Rich keywords in your prompts, keeping things simple starting with more detail, moving to less it should all feel obvious once you hear it and use it if it does, That means I'm doing my job as your instructor here let's talk about valuable features in AOR and in other tools that can boost what you can do with AI coding, So if we open our file Explorer here you'll notice this Ater YAML example file so let me close main and let's open that up I'll change the name so that it has this proper extension and this is what an AER configuration YAML file looks like
This is a reusable configuration file that AER will read from either from the root of your codebase or from your home directory to automatically set up your preferred configuration when you type AER There are many settings and flags here.
Let's walk through a few of the highlights.
First off you can set up your default model, right, so let's say you wanted to always start with the Oh one mini model you can comment model in and then type AER and now when it boots up Since it's in the root of this directory, you can see we're automatically starting the application with Oh one many with the best configuration, so this is great for model reuse we can comment that out and if you just scroll up here you can see we have the default Open a Api key.
We also have the setting for the anthropic Api key doing comment those out here.
Another great feature in AER is that you can set up default files, so if we search for file colon you can see we have this flag, we can comment this in we just go and close up and now we can just type a file so let's say we wanted to always have or read me right so this will now always activate, let's go and close AER and restart if we start AER now you can see that we automatically have read me added to our context window so this is a really powerful mechanism for always starting either with specific files, you can imagine you have documentation style, guides, patterns you know outside resources that you imported, that you always want to import as a guide on startup in AdR so this is a really powerful feature, Another great way to use this feature is to not add it to the file flag but to actually add it to the read flag
This makes AER start up with Read me as a read only file let's go to open up AER again and you can see we have this file added, but it is a read only file.
This is really important if you're adding files like documentation syntax guides, you know AI coding guides, This is a common convention you can set that all up in A or on boot up every single time by adding read only files in the AER configuration file.
This is a really powerful pattern.
Now when we write prompts we will not have the option to update this.
This is a great way to push your context management further and let A or know let the LM know what files you actually want to be changing vs strictly reading from.
We have the Suggest Shell command and I like to disable this throughout my code basis.
It's useful when you're starting out on projects to have a or suggest things, but I like to disable this so that I run the commands that I want to run There is this auto test flag and this test command.
This makes either run test after every single prompt you execute, so when you start moving fast with a coding, you can enable this and say you want to set PY test True After every prompt
A is going to fire off Pyte Test run the test, add it to its context window optionally and then based on the result of the test
If there's an error, it will automatically try to fix the air.
This is a great way to get more out of your E Coding assistant is a great way to move fast and have confidence in the work that you and your A coding assistant are doing.
A couple mentionable You can use a or in the browser by enabling Google Mode.
Here you can use a voice mode as well.
Links for all this stuff links for a configuration file documentation it will all be below in your loop box.
Using a reusable configuration means less set up work and more reusability across multiple code bases.
I hope you're seeing more and more why AER is a foundational AI coding tool it's made so that you can configure it, customize it and use it across many code bases with hundreds and thousands of files, I recommend you set up an AER configuration file in your home directory and on a per project basis in addition to using file configuration A or has a decent list of commands we have not covered yet, so let's hop back into a or here so as you saw in our reading we selected the mini model
At some point here we can change and list all the models that AER has available to us with these/models command So if we type/models and let's say we're looking for all the Sonnet models we can type Sonnet and hater will give us all the sonic models available to it.
It's important for this command that you specify some text here, otherwise it won't do a search.
So if we type such models and we look for a one, you can see all the variants of the Oh one model available to us at this time.
If we type model we can of course change our model.
Let's say we want to go to the preview which we're going to cover in our next video.
You can just type Slash model and then you can automatically change in your or chat to that model only to add read only files into the context window.
We saw this with the configuration file.
You can also do it using this command if we type Slash, read me if we type main if you only wanted to have these files in read only mode you can use instead of add, you can use/read only
This is a really powerful pattern for keeping your contact window clean, let's go ahead and run reset to clear both the chat window and our files so this runs/clear and/drop you can use/get to run any get command so if we run branch you can see that we have our main branch there
This is a Quick Way to anader just run arbitrary, get commands you can run/settings and this will print out all of your settings and your application state loaded from your configuration file and just all the defaults that are set in AER and you know any updates that you make inside the A or command you can see we're running GP for O model here you can use/run to run arbitrary Bash commands and then have the output of your commands attached right back to the AER windows so we just type Ls here you can see that we're listing all the files in our current directory do you want to have the output to the chat you can say yes and now AER will have that context in the chat window.
Right, so if we type/tokens
Now you can see we have a small chat history here with the information that we just ran above, so there are more commands if you type SL you know you can see a whole list of commands you can run here.
It's important to note that all A coding tools moving forward will have some version of these, you know, kind of foundational, low level essential commands I recommend you experiment here,
This is how you Can Boost Your Coding tool, productivity, you experiment, you play with this, try commands that you haven't before as all-important docs,
This is going to be below in your loop Boox I'll have links to AERs documentation for you to check out this lesson could not be complete if we didn't discuss how to keep up and how to focus on information that matters, that enables you to evolve with the AI industry right with the AI tech industry, A Tools are evolving every day from big tech to individual developers, a quitting tools are being created and improved on a daily basis at a rapid pace.
Engineering tools have always been different because they help us build more and better tools.
AI coding tools are the ultimate version of this because as these tools improve as aider cursor Z Getup co-pilot, get up spark all these variations of what is essentially UI wrapped in some code, wrapped in some prompts
As these tools improve, we improve and then we improve the tools and it creates this recursive feedback loop of immense productivity.
AER is a great example of this.
The creative Aider uses AER to build AER same with the Devon engineer, same with the cursor engineers.
Every engineer building these tools are getting meta level results out of it.
That means in order to keep up you must be using these tools and you must keep your eyes on the ecosystem.
You have made it to this course and you have invested in yourself.
This is a massive wind for you that will likely change the course of your engineering career, especially with the final half of this course that you are about to embark on.
I'm really excited to share the next generation coding ideas we have in the remaining half of this course.
You already know who I am, you already know what I do.
If not up-to-date, I'll be covering the best coding patterns and principles on the Youtube channel.
Link will be in your loop.
Boox Another reason AER was using this course is because the creator knows what he's talking about.
He has benchmarks, experience and data to back up all of his work.
I'm going to recommend the AER Leader Board so that you understand the best model to use to get the best echoing results.
This is updated regularly when new models are released.
I also recommend any blog release on the Aa website as well.
There are many resources and places to go.
The key is that you look for reliable sources of information from real builders and real engineers.
In the age of generator AI and the age of generator BI there will be endless junk and cheap derivative content.
Avoid these and look for the sources of experience, proof of value, experiments and data to back up their claims.
Now you know the most common ways you're likely to make mistakes with AI coding, with your AI coding assistant, But now you also know how to fix them balance, then boost first, make sure you're prompt Context and model are aligned Always start by writing low level prompts using IDK, which are information dense keywords we covered in lesson three and prompt phrases to write high-quality prompts as you progress you can play with mid to High Level prompts to save time, but whenever you get issues with a High Level coding prompt or you miss details, Always shift yourself back to the low level focus on getting things done, not saving a couple keystrokes here and there, then add only the context you need to solve the problem you're working on and think about the context from the perspective of your AI coding assistant before you run the prompt, think with this context and this prompt would I be able to solve this problem.
Imagine your Product Manager or a fellow engineer asked you to do something and they gave you this context and this prompt exactly would you be able to solve the problem is enhance the visization of our data top to bottom enough for you to really solve the problem.
Lastly, don't overuse reasoning models and don't go cheap on your base language model right now.
GPT for O and Sonnet 3.5 are solid, high performing base models.
This will change in the future, whatever AER has set up as the defaults.
I highly recommend in our next lesson we're going to run powerful reasoning models to generate tons of code with a couple new techniques that will expand the size of the swing you can take with your AI coding tools will show how planning is the key to accomplishing this.
Planning is the key to shipping massive amounts of code.
Congratulations on making it through Lesson four.
Give yourself a well deserved break and I'll see you in lesson five where we'll multiply your air coding abilities even further beyond.