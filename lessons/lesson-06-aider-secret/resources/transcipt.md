Welcome to Lesson six of principled AI coding.
This is the beginning of the edge.
This lesson, along with the next two, are your advanced lessons.
They consist of patterns myself.
Top engineers and Big Tech are using to generate massive amounts of code in fractions of the time it used to take just a couple years ago.
After this lesson you'll be welding AI coding tools and techniques like engineers of the future.
These lessons might break your mind a little bit they should.
This is the paradigm shift of AI coding.
This is the massive mental shift required to truly use AI coding at its Max capability.
In these lessons we start looking at our AI coding assistance like we look at Google maps fully trusting it, letting it do the work.
All we do is point and click at where we want to go.
We start handing the keys to the car to our AI coding assistants.
We let them take the wheel and simply point to where we want to go from the back seat.
Great information compounds it repeats
and then it compounds again.
We're taking everything we've learned once again and scaling it up.
Every principle you've learned stacks up on the previous principles.
Let me introduce you to the core topic and principle for this lesson.
A DW AI developer workflow.
This technique is so impactful it must also be the principle.
The tech ecosystem will have many names for this pattern.
What you call it isn't important.
What matters is that you understand and use this concept in your AI coding to scale your AI coding capabilities even further.
You can use AI Developer workflows to automate away entire classes of engineering tasks.
AI developer workflows hinge on a single requirement as long as there's a pattern, you can use ADWs to solve the problem once and for all.
After this lesson you will have the AI coding skills required to stop doing repetitive pattern based engineering work.
No more migration files, no more miles Api creation, no more templating, no more scaffolding, no more mindless testing the same thing in the same format over and over.
In this lesson we automate mindless engineering work.
In this lesson you'll learn how to build a reusable AI coding assistant built to solve one problem class extremely well, let's begin our lesson with our first principle kiss keep it simple, stupid.
Let's first understand ADWs AI developer workflows at a fundamental, simple level.
Let's open the terminal and if we type Alice here we can see our previous five code bases.
Let's go ahead and install the less than six codebase link will be in your loop Boox As always.
Now we'll see the end to our sixth codebase will open up.
Our favorite editor I'm going to use code here.
Let's run through the Read Me same set up as always will run UV Sync to install dependencies.
I'll copy Lesson Five's Environment file into this directory.
Go ahead, close and open up my terminal window again, so we have the environment variables fully loaded in the instance and then all run this command, our analyzed transcript method and you can run on any one of the previous text files I'll go ahead and run it on the third one and fantastic and now we're getting our output from our lesson five code base.
Right, so we have our counts.
Where were transcript analysis and if we want to, We can pass in the additional arguments like our output file or our chart, and we created this all in less than five, so re going to be building up and making added to our less than five code base here in less than six.
Now let me share Ader's secret with you in the set up instructions you can see we have a couple commands here you can see run AI developer workflows let's go ahead and copy this first version and let's just run this
and then we'll discuss what's happened after it executes.
I'm going to open up our terminal window, clear, paste this in and I'm going to fire this off
Okay so our AI developer workflow has just finished running and if we take a look at what's happened here, It looks like we've kicked off in eighter instance with a command.
What has our eighter instance done?
It's increased our version number from 0.1 point eleven to zero.one.twelve.
So let's go ahead and do a couple of things here.
First, let's confirm that change.
Let's open up a project file and you can see our version has incremented.
Now how is this happening?
Let's look at our ADW versioning file to understand how we were able to do that.
If we open up our file Explorer, open up the ADW directory, we have this versioning.python file.
Let's open this up and let's take a look at what's going on here.
AER secret is that you can AI code programmatically to automate entire classes of engineering work.
The implications of this are absolutely insanely massive.
This means you can run either like you would run any program you can pass in state and solve entire sets of engineering problems in a single command.
Let's dissect this file more closely to really understand what that means and how we can use this so we have this stand alone Python file.
It's a simple script and we have one method bump version at the top.
You can also see we're importing from AER if we open up our project file once again, you can see we actually have AER as a dependency for this project, this in combination with using Astral's UV Python Project Manager means that we can run this code UV, run Python or running arbitrary Python scripts with our dependencies and we're passing in the Python file.
Okay, so let's go ahead and dig into what is happening here.
We have bump type and bump type is going to be one of three where we have The Patch, minor and major and if you're not familiar, that's the different sections of the version, so we have The Patch here we have the minor here
and then we have the major version here
Okay so this defaults to patch
We didn't pass anything in there.
We're then validating that we do have this file so that we can actually update it, and more importantly, we're making sure that we are at the root of this project and now you'll see something very familiar and very, very cool now we're initializing the Big Three context prompt model We're showcasing the read only functionality, but more importantly, we have our context editable list, so we have our path to a Pie Project Taml file we're using read me as a read only file and then we have this simple High Level prompt
So we're saying, you know, Patch bump Pipe art Tamal version number
So this is just saying increment the version number we're using the GPT for O model
and then we're creating our AER coder instance we're passing in the model the editable file names read only file names we're turning auto commits to false so that we can commit ourselves.
This allows us to run GIT diffs on current unstaged files, and then we're running shell commands false.
We don't want either to ask us any questions while it's working through this automated workflow and then we're saying run the prompt
Okay so let's be completely clear about what's happening, we're starting a like this, a running AER with the GP O model We're adding my project to the contents window were adding Read me as a read only file and then we're running this prompt so we're saying Patch bump PY Project Tamil Version number This is what we're doing in this code and an automated fashion clear to instance out and run this code again
so I'll use control are for reference search I'll look for Python
and we'll just quite literally run this code again.
Okay if we open up our project file you can see that change got bumped, we now went from twelve to 13.
If I open up this file you can see we're at version 13, so I'm walking through this very slowly because I want to give you time to digest what is going on, we just automated a small task and we never have to do this again.
Okay, this is the beginning of the edge.
This simple example is showcasing what's coming next.
You can now, using an AI coding assistant like AER thinks that everything we've been working through, everything you've been learning throughout this course, you have the capabilities to write reusable AI coding assistants built to solve specific problems extraordinarily.
Well Okay, so I hope you start to digest how important this is and how impactful this is for you and your engineering work.
Let's scale this up so that we can better understand the impact of AI developer workflows.
Let's look at another use case.
They want to close this file Closer PY project and let's look at our new output type.python AI developer workflow
so here we have another workflow and if we collapse we can see the same structure it's just a Python script right, so we have this directory of AI developer workflows that can now operate and perform arbitrary tasks across this code base right and this is our same code base from you know, lesson five it's our transcript analysis code base.
Let's look at what new output type looks like, so you can see here instead of patch or minor or major, we're passing in an entire description, and what this will do here is actually make its way into our prompt, so let's go ahead and work our way down to that, we're making sure that we're calling this script from the root of the application and now we're setting up our editable files we're super familiar with this concept.
Right, we're setting up our contacts model and prompt we're lining our big three so that we can hit the big three bulls eye Every time this AI developer workflow runs, so we have contacts edible and we have a couple read only files.
We don't want to update these, but we do want our AI coding assistant to be able to read these files and then we have a concise low level prompt that updates two files we're using information tense keywords like update we have file references here we're saying add and then we have a detail here we want to add a new output format to the application based on the following DESC description
Okay, and then we're passing in the description from our CLI argument, right, and then we're going to say update Main to support the new output type and save with the correct extension of the new output type you can see here we're using the clawed 3.5 Sonnet model You can change this if you only want to use the Open AI for this code base we're going to be using both, so recommend you set those both up in your.environment
variable
so we're running the sonic model and that's the big three.
Right, we have our context, we have a prompt and we have a model here
so we're just going to create an AER AI coding instance, passes stuff in and then run the code.
Okay so let's go ahead and see what this looks like.
Right we now have a, a workflow that's doing more work for us.
Right let's see what this looks like.
So we'll say UV run Python
you so we have all of our A developer workflows under one directory were saying new output type and now we're going to pass in a description if you remember we have our type or command here that's going to, you know, read in a script, count the words run transcript analysis and then, if specified, if we have an output file it's going to read in both our transcript analysis and our word counts and create that proper output file format and then save it.
Okay.
So now we have an e developer workflow to automate this problem.
Write this problem of writing new output formats for our transcript analysis and our word count.
Let's create a new output type for HTML so we can write the description H Sul table Format output theap to want an Hml table will it enter and we'll let our AI developer Workflow do all the work for us.
You can see we have our new format as HTML method getting created and now we're updating main to support this new type and we'll see this come in right here perfect
it's asking us if we want transcript txt we don't will hit No.
So we can close this and take a look at our changes.
So we have our new Hl type and we have our new format as HTML and again because of the types and because of the context, right, because of our big Three bulls eye hit In our AI developer
Workflow We set up the context properly, we have the read only files where we were exposing our data types and our data types expose, you know, the exact structure of the parameters getting passed in to all of our output formats.
Right, if we open our output format and collapse, you can see we have a repeatable pattern in these functions with this specific naming pattern.
Right so this is one of those problems, you know how to do it, your entire engineering team knows how to do it, it's just a question of putting in the work and making it happen now you have the skills to completely automate tasks like this forever, so let's run this right it sounds nice
but if it doesn't run, it doesn't matter, so let's go ahead and hop that let's go and close these files, let's make sure that everything looks good, we have extension here I ll put type
and then we write that so it looks like we need to pass in a.html output file.
Right so it's going to do that, let's clear and let's run UV run main
it's actually just copy our execution here
so we have a previous version here.
Let's run instead of DAML will run.html and fire it off correct, so on and you can see we have output written to output transcript.html.
Okay so we see this file here we can open it
and as you can see here, we have our word counts and our transcript analysis and our summary in HTML format.
Our counts are in a table and I should have an HTML previewer here is open preview so here is our HTML preview.
Oh and I'm sorry for the blinding light here, but here's our HTML preview you can see we have our word count table right with our words from top to bottom
and then we have our transcript analysis here.
Right quick summary bullet highlights sense of analysis and keywords
So we now have this brand new format.
We ran one function that kicked off our AI developer Workflow
Right in our are developer workflow is a small piece of code that wraps in AI coding assistant that can take in parameters.
Right that's what an AI developer workflow is, it's a reusable AI coding assistant built to solve one problem extraordinarily.
Well
Okay so I hope you can see where this is going.
Right, I hope you can see everything you're learning here throughout this course, stacking up now you have the abilities to solve any class of engineering problem across your code bases in a reusable fashion, as long as there's a pattern you can deploy AWS AI developer workflows you can see we're using our great prompting structure.
There's no confusion here about what we're asking for, we said our contacts just as if we were running this a coding prompt ourself right in an eight or instance in the terminal we selected a great model that we know can solve this problem.
Well we're not going cheap here, we're also not going overkill with a powerful reasoning model, there's no reason for that for this problem set and they were passing in the description of the new output format type that we want generated, so the only true limitation here, the only true limitation Now is your imagination, your abilities to hit the big three poolside and the surrounding code that you have set up in your code base right, you obviously can't ask and you can't pass in a description here for something wacky that you don't have support for in your code base.
Okay, so let's run this again, let's show that these ADWs can actually do the heavy lifting for us for a specific problem set over and over and over to exact same workflow
so I'll just hit up and find that previous workflow we go and what I'm going to look for instead is I want an XML output format
Okay, so we don't have an XML format, I'm not going to specify any other detail, I'm just going to hand that off to the coding assistant.
I wanted to have it add an XML format, so it's running through the same thing, it's updating these two files, These prompts are crystal clear.
There's no confusion here, as we know from our previous lessons.
Let's go ahead and look at Main.
If we just search Exml, we can see this new block added We have format as Exl and now we have an XL version.
Okay, let's go ahead and once again kick this off and we're just going to update our output type because that's how we specify the, you know, the format type that we want to run will it enter and we're going to watch our directory here we should get a new output transcript.xml file that completed We now have Output transcript.xml let's click into it and would you look at that we now have our summary, our Blowet points keywords we have our word counts
and it's in a standardized validated XML format
So this problem of creating different formats for our transcript analysis.
It's solved right, it's done and of course over time code bases change, you might pass a new parameter into this method.
You'll want to make tweaks to your a developer workflow
that's fine, you can, it's completely accessible here, you can commit this code to your repository you can do anything you want with this
it's just code but this have a code is different, right, this code works for you, this code operates for you.
This code writes code for you, it solves problems for you.
This is an AI developer workflow.
This is advanced AI coding in just two commands we've generated a 1000 tokens, 680 characters and about a 100 lines of code COR and just two commands and of course you know you can come in here, you can make tweaks, you can run follow up AD HOC props or you can boot up an ater and
Since whenever you need to add this file as context, but there's nothing stopping you from going back to the base level you know, kind of day one AI coding lesson one lesson, two lesson three AI coding There's nothing stopping you from doing that in fact that is part of the full package of AI coding, but now you have a technique to help you scale your AI coding even further now you can write reusable AI coding assistance that solve a specific set of problems very well, let's push this further, let's incorporate key ideas from lesson five with the Spec prompt into the AI developer workflow.
Let's close these files will leave main open and let's look at our third a developer workflow.
We have this file new chart PY let's go and crank this open and let's walk through this the key idea I want to communicate to you here through these examples is that there are really no limits on what you can do inside of an ADW in AI developer workflow.
If we look at this new chart top Python file, there are several incredible techniques you can use here.
Every one of these techniques we've already covered were just building on this new concept of taking your hyper versatile coding assistant AER and placing it into code right, making it a reusable unit of programming let's walk through our new chart type AI develop a workflow we have description getting passed down as previously we're validating, we're in the right directory and then we're doing something awesome.
We have our spec directory and we can look through this and we can see we have specs.
Right is the same concept from lesson five.
If we click New Chart type you can see we have an entire marked down document surrounding the use case of creating new charts, So now we're taking the ideas of writing out great prompts to go in detail and solve a specific problem at scale.
Right, remember your spec prompt contains many prompts inside of it.
It contains your ending context, your beginning context implementation notes and then a mid and High Level objective of what you're trying to accomplish by running this prompt and remember your spec prompt you take this entire thing, you run it inside a powerful AI coding Assistant powered by reasoning model
right
so that it can work through each step step-by-step here we're doing the exact same thing we're loading in this new chart type spec prompt we're reading it and then we're replacing the description with the description we've passed in, We're making this spec prompt reusable inside of our AI developer workflow, Let's go and open this up if we just search description you can see it here in our first prompt
right the low level task here ordered to start to finish.
We're going to create a new chart type in Chartt Python, we're going to update Chart up Python, add a new function and we're continuing to use information dense keywords here to clearly communicate to our large language model and to our AI coding assistant
and we're saying that implements a new chart type base on the following description
right
and we have a simple string template that we're going to replace on this High Level here and you can imagine you have multiple string replaces you can pass in any arbitrary information you need to in your spec prompt to make your a coding assistant in this workflow as efficient and as dynamic as it needs to be right, we're creating that new chart type based on the description and then of course we're just doing a follow up Prompt Update Main PY
This is very similar to our new output type We're adding a little bit more detail, The key here is to showcase the idea that you can combine your spec prompt inside of a developer workflows In fact, you can put anything you want in this don't limit yourself, This is just code
so we're building on our prompt, We're then setting up our editable contacts We, of course, need Main and Cher and then a couple read only files where it's always helpful to have your data types Inside the context window We have our PYP project files so there a coding assistant knows what libraries it has available again here we're just doing great context management that we learned in lesson three we then setting up our prompt and this is really, really cool, so now we're setting up our model and you'll notice something interesting here we have two clawed 3.5 models Why is this?
This is because we're running in architect mode just as before with our Spec prompts and truly with any A coding assistant prompt using AER, we can run everything in architect mode for this simpler spec prompt with only two steps We don't need a powerful reasoning model to solve this problem.
Okay, but it does help to use Architect Mode to increase accuracy just a little bit and improve the performance of this AI developer workflow so you can see this coming in here we're using input yes to auto approve the suggestions from the architect model, otherwise you'll need to manually hit Yes, and we want to develop a workflow to automatically just run, do the work, get it all done for us without intervention, but then of course passing in our context we're using auto commit false so that we can commit this change ourselves, using suggestion, commands false and then, of course at The Bottom we're just saying Coder got wrong so we're just kicking our AI coding system off and that's it.
So let's go ahead and generate a new chart.
Let's prove that this has solved chart creation and if you remember we have this chart.python file we can collapse and you can see you know right now we just have three chart types bar, pie line so let's go ahead, use this AD developer workflow and generate a new chart type UV run Python ADW new chart
W PY
Right, so now that's this file and we're going to pass in a description so description here is I want a bowl chart
and I want it to see scale size of bubbles based on word frequency.
I want the largest bubble to be fifth of the available space.
Word counts I exaggerate bubble sizes, use colors to indicate different count ranges, overlay and I want the words to be on top of each bubble.
So say overlay the words in the center of each bubble
ok so we want to bubble chart here so let's pass this
and we're passing this prompt right, we're passing this into our a developer workflow
Now the editor is actually going in and making the changes.
Both of these changes were made and now we can execute this code so let's go and take a look we now have a new create bubble chart method, We have some colors here we have sizes and this looks great overall
let's go ahead and look at our main because in our main we now should have there we go, we have a brand new Create bubble chart method If our chart type is specified, so let's goad and run this right, let's go ahead and run UV run main we're going to pass in as always a transcript file, Let me just go and load the previous version from Main here and so run this we will create a YAML and then we'll use chart type bubble G
So if you open up our Foll Explorer We now have bubble chart
PNG Let's crank this open and you can see here we automatically generated a bubble chart
and so you know you might look at this and you might go Okay there are changes that need to happen here I want to scale up the sizes, no problem at all.
Right you can always kick off an AD HOC, a coding assistant right at or sonnet we can add our chart and you know, we can say increase the sizes of our bubbles X five Right, just run a simple High Level prompt there one pound the context window not a lot to confuse
and you can see there we're just scaling up the size if we know close this, rerun that code we can always come in after this is run and make arbitrary changes there.
Right so you see this got scaled up you see, these are properly colored based on their size and we now have this bubble chart
right
and we are running random variants so we can just go ahead and kick this off again
and we should get another version of this, you know, we might want to centralize our bubble charts closer to the center, we might want to change the colors these are all things that we can do in follow up prompts and these are all things we could have mentioned in the details for our original prompt for a developer workflow
Right, let's just go ahead, let's get one more version of this I want to see the another randomized version
Okay, nice
so you know you can see we have another version, Many changes you can make here, but the point is made right, we can now generate many different types of charts in a single command.
It's also important to note because we have this clean separation between our ADW and our Spec prompt, We can always come in to this file and update our intended implementation.
This document is now defining how we can solve the problem of creating new chart types now and moving forward.
We're now using and wielding multiple AI agents, multiple AI coding assistants to solve different problems for us automatically.
This is, this is fully automated, It's all about how great of a prompt can you create?
And again back to the fundamentals of principle data coding.
Are you passing in the right information, the right context model and prompt into your AI coding assist.
Right our and Deoper workflows purpose is to define the A coding assistant details so that you can hit the big three.
Right, you want to be hitting the context model and prompt the spec prompt allows us to go in deeper, detailed, it allows us to make a prompt more dynamic, more rich and it allows us to scale up the size of the problems we can solve and that's a good delineation for deciding if you want to use expect prompt with your ADW with your A developer workflow how big is the problem you're solving, so let's go ahead and run this again.
Let's just go ahead and hit up a few times here and let's go ahead and create a new chart
right
so I want a variant of I don't know, I want a top pie pie chart of word counts with the top three words exploded for emphasis.
Okay, so I want our classic pie chart, but I want the top three counts of the pie chart to kind of jump out of the chart so this is something that I can just think and hand off to our AI developer workflow.
Right, why, because we've solved the problem type completely.
Right, this class of problems is solved, so our architect just drafted the changes.
Our editor is now making the changes and you can see Create top pie chart getting created there we should see an explode keyword there is using Map plot lib.
Changes are complete.
Two files were automatically edited for us.
Let's go ahead and execute this so we want to run basically the same thing as before but want to use let's see what type was created for us.
We have top pie let's run with the chart type Top pie
there's our usual run down, there's our saved file top pie chart.pngg let's open that up and there it is.
Right, so just as we ask for, let's zoom in a little bit you can see our top three pie slices are exploded out right, so this is an attribute of the Map Plot, Lib, Pie chart library and of course, our AI coding assistant has access to our project dependencies.
Right, so there's the project path getting passed into the read only and our project path contains what libraries are available,
Right, so of course as you know, we have not plot Web here, just like we discussed in lesson three, that's just part of great context management our a coding assistant in our AI developer workflow using the Spec prompt it has everything it needs to solve this problem once and for all so this is fantastic right we can literally solve any version of this problem, so long as we have given all the information needed to solve it, let's run another one just because we can I want a radial bar chart and keep note, you know, keep in mind all my descriptions here they aside from the first description all my descriptions I'm passing into this AI developer workflow are relatively simple and short.
Right, I'm saying create a radio bar chart, I'm really leaning on the technology and the libraries that we have, which is what you should be doing
and so you can see our architect is walking through the draft looks like we have a nice radial charting generator there thanks to Sonnet and then our editor agent right also running the Sonnet model is actually executing running this if we scroll down here we can see those edits have come in, let's go ahead, take a look at the code should always be reviewing your code as you can see as we build out our AI coding skills we're turning into commanders of compute commanders of AI Coding Assistance and our role is turning into less you know, type less lines of code and more review, more, think more plan
Right we're turning into an Engineering Manager, a Product Manager a higher level engineer that can do massively more than they could before while maintaining control over the product.
Right, we're getting the best of both worlds a lot of times as an engineer, you're too boggled down in the low level details.
We're now handing that off to be super effective and to have a larger vision of the product users, so on and so forth.
Right now we can do both, we can think about the product, we can think High Level
and then we can go and pass off that low level work to our suite of AI coding assistance, Our suite of reusable economic assistance via this new AI developer workflow pattern.
Right, so anyway, let's look at this, we knew how we now have radial and let's go into this just quickly reviewing the code, just a quick draft and it looks great, let's go ahead and execute This will hit up a couple times and our chart type is Radio will fire that off and again our model, our assistant has everything it needs, we've set it up for success.
We've invested in the spec prompt, we've invested in great information, tense keywords at the right level, right, some of these are High Level, Some of these are low level, we have High Level task descriptions Low level prompts file names clean function names, context It's all coming together, we're writing code with AI we're moving faster, we're solving entire classes of problems we're going to see in code bases once and for all Okay, so that just got written and now we have this radio chart and wow look at that, you know you can see we have this cool chart here with the words frequencies looks like up to one
and you know these three kind of tears
and
yeah we have this chart generated, it's done and it's in a workflow we can effectively generate any type of chart we want now with this AI developer workflow, so it's done, the work is done, This is advanced AI Coding in Combination with Spect prompts and all the other work we've been doing.
If you understand the technique, you now have access to asymmetric engineering over the next couple years, as some engineers are getting transition out because they can't keep up with ideas like this and they can't transition to leaning on air coing assistance and to focusing on the what instead of the how you are going to be getting so much more done than your peers with this information.
If you understand this technique, you have access to asymmetric engineering.
You have now solved this problem, moving forward, this is your lead, this is your massive advantage to use and you can will this, You can use these techniques throughout any code base you operate in?
Right, this is just it's a new patterns in New Paradigm ADWs a develop workflows in combination with powerful resume models.
Spect prompts I hope you can see it all stacking up.
I hope you can see this all coming together.
You will not be the same engineer if you deploy these concepts.
If you practice these concepts as you're digesting this information, you might wonder Okay, when should I use an ADW over a spec prompt and when should you use a spec prompt over a basic AI coding instance?
Right, let's go and talk about that right now, let's let's dissect this a little bit and talk about when to choose between each so here's how you can break this down.
You should use a regular A coding session in AER for any tool really when you are doing quick fixes, when you're exploring code, When you're solving small tasks you're making tweaks, you're rapidly prototyping and you're just making AD HOC one off adjustments right booting up this instance putting up in a coding instance like this it's optimal for bug fixes or when you're working on a feature that doesn't have a clear solution.
Right, you're not exactly sure how the implementation will work, so the kind of standard a code instance session allows you to be flexible, allows you to experiment and adjust right, you can quickly move your context around, you can do all types of things right, this will be the go to as you are skilling up as you're upskilling as you're learning how to use your A coding assistant, But this is not over time where you should be spending the most of your time you should be spending most of your time writing Spec prompts so let's open up that spect prompt Once again.
Spectrums are best for medium to large tasks that you can plan from start to finish.
Spect prompts are designed to offer more structure and allow you to solve larger problems by, you know, creating a more detailed outline and of course, a more detailed plan We dove into this and less than five and we saw how valuable it can be to write out everything to think through everything that you're going to do in your coding session and then to hand this process off to a powerful reasoning model running on Aa running in architect mode In this workflow we only have two steps so it's not alter impactful here.
The fewer steps, the less important it is that you use spect props, but if you're solving a problem that requires more than 345 props and you know what they are, you should always be using the Spec Prom
This is where you want to be spending the most of your time.
Why is that?
It's because as powerful reasoning models improve and as our AI coding assistance improve, they'll be able to take the instructions you give it and solve the problem and write the code and generate the documentation, they'll be able to do all of it, and so what you don't want to do is stay in the instance again.
This is good for quick fixes, code exploration, smaller things, bug fixes, but the more time I've spent diving into these concepts, diving into AI coding patterns and paradigms, the more time I spend not coding but thinking and planning and designing architecture
Right, this is where it's all going and this is the critical mindset shift that you should be thinking a lot about as an engineer we are, we're moving from the low level details of how to what right
It's more about the High Level Can you take the information?
Can you take the pieces and can you put them together and then can you hand it off to an AI assistant to do tens and hundreds of times faster than it will take you, depending on how early you're consuming this lesson and consuming this course you might be thinking, man, it seems like it's a lot to go through and plan everything and I want to just you know, take a moment to address that I hear there are some cases where you're right, but over time you will become more and more wrong the true essence of the Speck prompt is that it allows you to scale up to the capabilities of powerful reasoning models and powerful base models if you avoid getting the practice and the reps of building these great plans out not only are you missing out on thinking through things and to end, but you're missing out on the insane capabilities you will unlock with powerful models This is just a fact models will not stop improving.
That means that the only limitation is our abilities to fully utilize them.
The Spec prompt gives you those abilities to fully utilize the potential.
If you need a refresher revisit lesson five really take your time with the stuff.
It's a lot and again the biggest thing with these advanced lessons The biggest bottleneck is going to be you transitioning into thinking about engineering in this new way where you're handing off all the, how all the details to your A coding a** system leaving you to focus on the higher level objectives, leaving you to focus on breaking things down and communicating what you want done with your a coding assistant so that was a long ramble, but I highly recommend you spend the most of your time as you're evolving, as you're developing your A Coding Skills Spending your time with Spec prompts is the way to go so lastly we have AI developer Workflows You can use a developer workflows whenever you encounter recurring patterns or repeatable structures in your code base.
This is great for tasks of any size where there's a recognizable repeatable pattern.
You can think of things like Api endpoint creation, database migrations, type generation, templated function structures you saw, is create new output types.
If we open up our output format you can see there's structure here right there's a pattern here Format as string transcript analysis word counts format is JSON transcript analysis word counts right, three makes a pattern we have three of these and then we can automatically continue to generate this pattern, moving forward by just tweaking couple of variables in this case a single variable.
Right, we're saying I want XML, I want HTML
and it's important to call out that we can tweak this even further, right, there are many variants you can generate with HTML, so you want to be thinking about ADWs When you have repeatable patterns in your code base and when you see a certain type of problem or a certain type of task come up for the third time, right, three times makes a pattern ADWs are ultra, ultra powerful and as soon as you put the effort to to automate you know, one or two developer workflows with ADWs you're going to have a massive breakthrough moment.
These advanced lessons are all about Me Helping you get to those break through moments.
Using these next generation AI coding techniques and patterns, A developer workflows are a massive unlocked You can deploy these across any code base and this is all thanks to AERs simple secret that at this point in time in the air coding ecosystem and the air coding timeline is completely under.
appreciated.
Now you've seen this, we've talked about it here, this is yours now this is your technique, this is your knowledge, this is your information as you know in the age of General AI there's going to be so much junk and so much garbage what I've put together here in this course in this lesson is the oil is the purest, most valuable information I've been working on for over two years now using these tools you can now take a coding assistance, Wrap them in a small script and solve entire sets of problems with a single command using AI Developer workflows if you see a pattern if you know what the context will be and if there is a model powerful enough to get the job done and trust me for most problems, you'll see in code bases I can guarantee you there's a model that can help you solve that problem so you want to be using ADWs when you see repeatable recurring patterns where there's structure in your code base set up to solve that problem already.
Start with regular A coding sessions for non repeating tasks or unknown problems, or when you don't know the end to end solution, Use Spec prompts as much as you can to plan out work Remember you can always plan a spec prompt and then fall back to an AI coding session That's the most probable thing to happen you by prompt supply at your work and execute medium to large tasks that have clarity and that you can see and to end the more time you spend a coding, the more you should be planning your work and handing it off to powerful AI coding assistants using powerful reasoning models all you do is say here's the document, here's the spec, Here's the list of prompts I want you to complete, you can deploy ADWs for tasks where patterns are merging This lets you automate streamline and scale repeatable solutions across any code base you're operating in for more complex AI developer workflows, you can embed spec Prompts Inside of Your a coding assistant and pass in variables just like we did in our new chart example
Right we replaced the description and this allowed us to make our spec prompt built for solving new chart types, reusable and dynamic We use an Air Architect instance with two call 3.5 sonnet versions because our spec prompt only had a few you know, only had two steps I recommend when you get to 345 plus you switch to a powerful reasoning model Remember, try to avoid the common pitfalls you don't want to go too cheap you always want to start with the best model and then downscale from there As AI models continue to improve and As AI coding assistants like AER continue to improve what you can do with AI developer workflows and what you can accomplish with Spec prompts will only continue to expand the types of problems you'll be able to solve in a reusable, scaled fashion with AI coding assistance will only continue to expand.
That's why it's so important that you practice these advanced AI coding techniques, so ADWs really have no limit.
The only limitation is what you can think of and what your codebase allows you to do.
Right, let's open up our original patch.
Right use this codebase use the content, Use the links below to understand ADWs to understand their true capabilities.
This is reusable problem solving This is a small piece of software that can solve problems as you would in your code base.
Keep it simple, always fall back to the essential principles right hit the big three Avoid common pitfalls, scale things up with the spec prompt, solve problems and reusable way with the ADW with the AI Developer Workflow You can automatically generate tests in specific formats you can generate SQL migrations you can generate Api endpoints in specific structures with specific decorators and auxiliary information you can automatically build data transfer layers and so much more as I mentioned the true bottleneck with a coding is your abilities to take High Quality AI coding prompts, Spec prompts and now ADWs and use them to solve real problems.
It's time to practice, it's time to get reps in.
You need to be using this up to understand what it can really do for you and your engineering and your career.
A massive signal for when you should create an ADW is when you're writing the same code for the third time with a slight variation of a task or problem.
Once you start seeing these, you'll start deploying ADWs and you'll start saving massive amounts of time, you'll begin to transfer the work you're doing more and more to your AI coding assistant, You'll be improving the productivity for yourself and other engineers if you choose to share these techniques with them.
That choice is yours.
In the age of generative AI, every advantage you have as an engineer is critically important.
Now, once again, I recommend you take a break and take time to think through how you can use ADWs right now to automate something in a code base you're working in.
This concept can dramatically increase your engineering output by solving repeat problems.
Repeat tasks in your code base if the problems you're solving have a pattern.
AI developer workflows are likely worth the investment.
Congratulations on making it to the end of less than six.
I know the content here is getting dense and less than seven are second to last lesson.
We continue exploring advanced AI coding techniques that will change the way you engineer great work here and I'll see you in less than seven.