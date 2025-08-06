Welcome to Lesson V of principled AI coding.
In this lesson you'll learn how to consistently generate massive amounts of code with the single prompt In engineering, there are always bottlenecks and limitations before opening eyes, reasoning models and entropics Clause 3.5 the LLMs still had major limitations they would hallucinate, cause issues and couldn't solve problems consistently.
That is no longer the case now it's our abilities that are the bottleneck.
The question is, now what can we do to unlock the full potential of these incredible models?
Spec based AI coding is a technique you can use to capture more of the potential of these models.
In this lesson you'll learn to use the speck prompt.
A spec is a specification which is also simply known as a plan.
If you're a senior plus engineer, you're luckily familiar with planning your work, creating architecture DOCs and figuring out what needs to be done before you do it.
Planning your work is a massively important skill for AI coding.
Why, because powerful reasoning models can do more, the true limitation is in what we can ask it to do.
Writing a great plan and passing it to your reasoning model enables you to tap into its true capabilities.
Everything we've done so far in this course has led us to this lesson.
A great deal of a coding in the future will likely use the patterns we discuss in this lesson, the principle and key information behind this lesson is simple, but I have to warn you this is the lesson where things can become challenging, there is a large mental shift needed to use the principle and information in this lesson this is where we really start deviating from traditional coding into something completely different if you're able to digest what I have to offer in this lesson you will evolve into an engineer of the future you'll wield massive amounts of compute to get more done in a fraction of the time it takes another engineer, It's incredible what you can do when you invest in yourself and when you invest in a great plan you can use to drive results, Let's start with the principle, the plan is the prompt plans prompt and that means great planning is great prompting in this lesson we are going to stop firing AD HOC high and low level promps to accomplish one task at a time instead will use powerful reasoning models like Openai O one model series will combine it with a two step prompting mode built into AER and most importantly, will write a comprehensive spec also known as a plan which will detail exactly what we want done so just to recap, There are three big ideas we're going to combine in this lesson to make your AI coding abilities go Parabolic reasoning models, spec documents and architect mode.
Let's break down exactly what these are and how they work together.
Advanced reasoning models have the capabilities to work through and iterate over your prompts, context and code.
This drastically differs from traditional models, where they're effectively blurting out the first answer they think of.
There are tools that chain together prompts and their outputs to improve the result.
This is a technique known as prompt chaining or chain of thought.
We're going to use AER's version of this called Architect Mode.
With this mode you use two models, one to draft changes and the second to make edits.
Given the draft, this mode alone will drastically boost the accuracy of your code generation.
But when we combine architect mode with powerful reasoning models and a great plan, we get something extraordinary, a powerful model that can reason and think through the changes you want acting as an architect and then a faster base model like Claude 3.5 Sonnet that can edit code more accurately thanks to the work of the architect reasoning model when you put these three innovations together you'll generate more code than ever was thought possible before in record times with minimal errors we couldn't discuss reasoning models and architect mode until now because we've been building up our AI coding skills multi file Context management using information dense keywords prompt phrases, balancing high and low prompts and avoiding pitfalls are key to being able to properly will reasoning models at scale with the spec prompt making mistakes with reasoning models is more expensive in both time and monetary costs I want to note that what we're really doing here is continuing the trend of learning how to best communicate the most work to our AI coding assistant to generate the outcomes we're looking for over each lesson we're generating more and more of what we want done using our AI coding assistant using the right coding principles The right model context prompt and techniques A big piece of what engineers MISSIs the true capabilities of these reasoning models you can do so much, you can build so quickly that it's hard to mentally wrap your mind around it's hard to make the mental shift from writing code by hand, then writing code with prompts to then thinking through everything you want done planning your work gathering context, gathering documentation and then writing out each step in detail before you hand it off to a powerful reasoning model that does all the heavy lifting for you, but if you can do this if you can push through this lesson you will be AI coding like very few can and you'll be ahead of the curve.
This is where this course really begins to accelerate and as we discussed, AI coding is a new skill, It requires a different mindset.
You're shifting from the how to the what you're becoming a commander of compute, where the compute is your language model and your AI coding assistant, The only missing thing is the techniques to truly capitalize on powerful reasoning models and the mindset shift required to scale up your AI coding, that's what you learn in this video we're scaling up your AI coding abilities the key takeaway here is that with the techniques will discuss in this video the only bottleneck preventing 101,000 plus line code generations across 51020 files is you?
It's your imagination and it's your skills here in this lesson you'll widen this bottleneck and tap into the capabilities of powerful reasoning models.
Keep this principle close.
Great planning is now great prompting planning equals prompting let me show you exactly what I mean by this and how it can truly change the way you engineer let's open the terminal.
If we run Ls we can see our previous four code bases.
Let's clone in the lesson Five Code Base Link will be in your Loop box C DN to our lesson five codebase and let's open your favorite editor here and run code perusual I'll copy my.in file from the previous lessons code base.
Let's open up the read me and run through the setup instructions.
So right away we will run UV Sync to install our Python dependencies and for this code base, I recommend you set up both the open AI Api Key and your Anthropic Api key using models from both of these providers will give us optimal results.
Now we can run our primary script with UV run Main
and you should see Hello AI world.
If you open up the main file, you'll see a simple bare bones Python application.
Fantastic now what are we doing and lesson five to Learn Spec prompting Specification prompting We're going to rebuild our transcript Analytics application from scratch with just two spec prompts and a few follow up prompts from a base model.
We're going to recreate everything we've done in the previous four lessons in a fraction of the time and effort.
Now inside you read me, you'll notice a new A or command.
I'm going to go ahead and copy this and paste it into my terminal window and let's walk through this so this is how you run AER in architect mode, you can see I'm specifying two models, I'm running the Preview model in architect mode, and then I'll specify Claude 3.5 Sonnet As our editor Model AER should give you a message like this you can see Main model is preview editor model is Claude 3.5
I recommend preview or if that's available to you, combined with claw 3.5 sonnet for optimal results But if you don't have access or don't want to get access to anthropic you can run exclusively with Openai based models using the one preview and architect flag alone you also can use O one many but it is not recommended as many as quite a bit more error prone keep in mind the cow pitfall of going cheap at the expense of experience we discussed in lesson four
I know the reasoning models are particularly expensive, but using them and gaining experience with them is more important for what's coming next you're going to want to be ready for the next generation models that are coming after these if you don't practice with these models and understand it.
How will you know what you can do?
We're going to use a one preview, but if you have access to the newer oh one model or anything beyond that, I highly recommend you use that Now you'll notice here in our File Explorer we have this new directory named Specs.
Let's go ahead and open this up and let's start with the Transcript Analytics Zero markdown file.
The Spec directory is where you can store your specification files.
This is where you can store your plans now I'm going to collapse.
This plans that we can see the High Level sections and let's walk through what a specification document looks like.
This is what we're going to use to generate massive amounts of code, so let's take a look at the structure at the top we have our High Level objective Create a Ci Transcript Analytics application.
If we close this and open our mid level objective, you can see five more detailed bullet points Build a Python MVP type or Ci application, Accept the path to a file count the frequency of each word in the file use Open AI Chat Rich print the frequency so you can see here we're getting a little bit more detailed we're setting up some more information for our reasoning model and for our AI coding assistant.
Now let's talk about the implementation notes this where we can add detailed AD HOC information to let our model know specific details of how we want this code to be generated.
We're saying don't import or suggest any external libraries.
See our PY project file for our dependencies, so you know if we open that up we already have our dependencies all set up here and we're going to add this file as context so that our reasoning model knows what's available, we have a comment, Every function implementation Note for type or commands we want usage examples starting with UV R main Since we're using Astral's UV as our Python package manager, and then we have two additional implementation notes, Right, just kind of highlighting and guiding our reasoning model so this is a place where you can add information and rules that you want your AI coding assistant to follow for this specific feature.
Now let's talk about the context.
Our context details are exact context window so what files were going to want in our context window during the beginning of the task execution and then the end so you can see how this can be really valuable for the reasoning model.
We're explicitly stating what files it will have available, and then we're also stating what files need to be created by the end of the execution of this prompt.
This is also a really important section because it helps you, the engineer work through what you'll expect from the beginning to the end, So the last and most important section is our low level tasks.
Let's go ahead and take a look at what this looks like.
These are individual tasks broken up into a numbered list and guess what each item is a High Level and a low level prompt.
That's right, the Spec prompt is effectively a set of directions followed by a list of prompts.
This is an ultra important structure.
If we look through this you can see we have marked down formatted eighter code blocks.
If we just go ahead and collapse all these, you can see we have four inter code blocks and then one block of explicit Python code.
So let's just talk about this block for a second because this is really important.
This is where all the magic happens.
We're taking everything we've learned and scaling it up by creating an ordered list of prompts.
In this section alone, you can see everything you've learned so far is compounding into this powerful spec prompt.
The huge breakthrough here is our reasoning model is capable of generating every single task we have here because it's iterating over the response that it's generating right, that's the big breakthrough with the reasoning models It's running its own internal chain of thought, also known as a prompt chain, so a key aspect of the low level task is that it's ordered from start to finish.
So why is it important that it's ordered, ordered task lets us do a couple of things they allow us to communicate the individual props and their outcome in a stacking, compounding fashion so that we can refer to the content and previous prompts and later prompts Let me show you exactly what I mean here if we open up our step three
Remember we create a word counter we filter out some characters
and then we limit based on threshold if we open this
and then we open up our data types, So if we open up step two and step three you can see here we have this word counts pedantic type and in step three we're explicitly referencing work done in step two this is ultra important because we're now passing our information dense keywords Remember this is a type information dense keyword
We're taking this word counts and explicitly using it in the return type of this function.
Right.
So when our a coding assistant is looking through this, when a reasoning model is working through this, it knows that our word counter should take in scripts mid, count, threshold and then return a word counts which it's already seen right in this version of our transcript application.
We're defining this type to contain our count to word map, and then we were specifying that type type based AI coding is a massive, powerful unlock Data types Interfaces classes are a fantastic way to communicate information to your large language model as discussed and lesson three, these are information dense keywords right types, functions, variables, files, These are all things that have strong reference points, Strong locations and strong meaning associated with them are ordered.
Low level tasks allow us to communicate information across our prompts.
Right, which of course is absolutely essential.
So the second reason that these ordered low level tasks are important is because Since we have explicit references to these, we can add the Spec prompt file itself as context and refer to specific tasks we'll see exactly what that looks like in just a moment here Since word count was defined as an explicit type there is no confusion for the LM about where or what this thing is, this is the power of having a list of tasks that can be executed by powerful reasoning model in order thanks to our specification document
so if we just look at what's going on in each one of these tasks all we need to do is look at the High Level we don't even need to look at the low level prompt We're creating our common word blacklist just as we had before creating some data types creating our word counter functionality
and then we're running our LLM chat call
and it's important to note you don't need to write a prompt in every single one of these tasks you can just place code and this is something that's likely to happen as you're pulling in third Party documentation or working on a feature you'll be working with existing code, so whenever you need to you can just drop in a block of code where we can still say as a comment here you know, create this file, we have a nice simple low level prompt here, but then we're just referencing a block of code so we have that as our fourth task and then in our last task we're putting it all together in our main file, Right, so that's when we're actually going to be updating main and filling out all the content, all the code that was just generated so without further ADO, let's go ahead and fire this spec prompt off so we can open up the terminal.
Let's go ahead and go to our context section to know what we need to add to our a coding assistant and we're going to add main
and then we're going to read only add PY project Tamil.
This has our dependencies and this gives our reasoning model the information it needs to know what dependencies it has access to and then finally to run this we just literally copy our entire spec, prompt and paste it in and let's execute reasoning models.
Take some time to execute because they are, you know, are quotes thinking through the prompt context and the result, we can expect 20 seconds to a minute, depending on the size and complexity of the spec prompt a cut here and will return when it's completed.
Okay, fantastic so we have a completion here, let's just go ahead and review our changes task by task, so as we start scrolling up you can see our last task was to create the analyzed transcript function in main and put everything together so right away you can see this is done really, really well this piece looks great let's keep scrolling up, you can see we're setting up a type or instance and type or it's a Python library you can use to build Ci applications, so you can see step five Great
it's lined up its reasoning with our High Level tasks and the code so let's keeps growing up here you can see we have our step four right, which is let me go and open up step for here let's look right so step for creating our LM function using the existing code block below without making any changes and this is something that I explicitly added a couple of times when you're referencing code specifically, it's always good to just say you know, don't make any changes, just use the code as is so you can see here still importing everything and it's using the, you know, structured outputs format from Opening eye
This is great and if we scroll up right so that step four and we look at our word counter
Right, so step three was our word
counter filter out and limit by so we can see that right here, right when go ahead and open up this prompt you can see here we're saying create this file we're still using all of our great low level prompt information, dense keyword practices, so we have, you know, create we have a file reference, We have a new function with parameters with default value with a concrete return type that was specified in task to and then we have, of course, our details right, so we're still sticking to everything we've learned we have locations, actions and details here in this great prompt and that generated the exact result we're looking for here Right, filter our common words from our blacklist and again our blacklist here common words
blacklist
This is a variable information Dense keyword that was created in step one.
Right so in step one you can see here create constants and they were saying create this variable and then in step three we are referencing this variable exactly, so we're sticking to her great prompting practices, we learned in lesson three we can see all that code is working there.
Filter sort descending, then we return that actual object structure.
Right, this new word counts object structure
so that's fantastic.
The raising model is doing a ton of work for us.
If we look at step two, we are asking it to generate our transcript analysis and our word counts for us, right, so these are two pedantic types detailed in step two.
So this looks fantastic and finally step one of course just create our blacklist and we see this here
and you know it was able to infer and 50 more common words so that's it.
But our reasoning model, the powerful O One reasoning model, worked through a ton of changes for us thanks to our detailed specification.
Prompt right thanks to our detailed plan and I hope you can start to see the value proposition of planning your work and handing it off to a powerful reasoning model.
So we are in architect mode, so er did not just go ahead and make these changes, what's going to happen is we're going to hit why enter and now our architect is going to hand off this draft, every one of these draft changes to our editor model, which is going to be our claw 2.5 sonnets so hit yes
and we'll go ahead and let Sonnet actually create these changes now
right so if we open up our explorer.
Nothing's actually been done yet.
Right, that was just the code draft.
Sona is going to actually edit these files and then ask us if it's Okay to generate the files, so it's asking us to create our new contents file, I'm going to say yes, of course data types
Yes, Work Counter
yes, LM
yes look at that a five file multiple edit just went through and we'll hit yes to all and so now we have all these files in our context window.
Let's review the changes so in the poll explorer you can see all those files exist.
Now you can see our main looks fantastic let's look at LM we have that exact code block we asked for data types, we have our two types word counts, transcript analysis constants We have our common words blacklist array and then in Word Counter we have our word counting logic
right
and of course it returns just as we specified in our function definition, it has the exact definition we're looking for and the correct return.
So our reasoning model in architect mode just did a ton of work for us and I want to say something that might sound a little jarring or scary or exciting.
This is a small spec prompt this is a small plan.
We're only asking for five changes.
You can imagine you're working on a feature on a large production code base.
This can easily be 1015, 20 code changes, each one of them being their own great prompt.
Right and that's that's important piece if you're a bad prompt here, the reason model can and will make mistakes.
In fact, with the Spec prompt, you should expect to run another eight or instance to clean up anything that needs to be changed.
So moment of truth let's go ahead and just try to run our generated code first try so we're going to open up a new terminal window here and it generated example use DOCs for me
so I'm just going to copy this, paste it and let's go ahead and run it.
Okay, so we do have one issue here in our run command.
We are expecting a main function, so we're going to boot up in an additional eighter instance, we're going to resist the urge to make the change manually.
We really want to be making that mindset shift away from manual code changes to going to run a new AER instance here with aerd Sonnet.
This will automatically boot up either with the cloth.5 sonnet and Since and what I'll do here is I'll just add main and over run a quick prompt create DEA main
so that's it, so we're running into a typeer error here when you only have a single typeer method you don't need to explicitly refer to the function so we're just going to drop this and kick it off again.
There we go, minus a couple hiccups you can see all the actual code right, all the feature related code was generated perfectly.
This was all thanks to our reasoning model, looping through and thinking.
The changes are Specification document which detailed everything we want done and of course, our AER architect mode right, which improves quoting accuracy because we're running a powerful reasoning model to draft the changes and then a great base model to write the changes given the architects draft, so this is very powerful AI coding let's take a look at this main file, Look at how beautiful this code is.
Right it's it's exactly how we asked it to be.
Right it's exactly right, there's some small things, right, some missing imports that's all small, simple things that traditional code tooling can handle for us.
So let's finish out our transcript Analytics application by writing a another spec prompt by hand using a reusable template, so that's another advantage of these spec prompts right, they have structure to them, they have format to them right there's a flow to these prompts if we open up Spec template.markdown
you'll be able to see a template of our previous file read
So what's going to just collapse you can see just a clean template of everything we just did so what we're going to do here is walk through making a couple additional changes to our transcript analysis application, If you remember we were also generating charts and we were also generating an output file type
So we're going to go ahead and write a spec prompt by hand to generate that so first thing I want to do here is copy the spec template and let's give it a name so it's going to be transcript Analytics called the one and that's fine.
Okay.
So we have this file now, so let's walk through this, let's get another rep in so that we can really understand how powerful writing a detailed plan with a list of prompts can be when we hand it off to a powerful reasoning model to truly master a coding you want to let your AI assistant do the work for you.
All we're doing now is investing more time up front to communicate properly what we want done through a plan.
Okay, so let's just go out and walk through this, there's going to be a transcript Analytics and let me close our file, explore here updates and we can go ahead and say chart and output file
Okay
and we have a little sub comment here you can remove this if you want, I'm going to go ahead and leave this end and let's talk about the High Level objective.
Right, so now we're just filling out this spec document so High Level objective we want to add charting and output file functionality to to the Ci transcript application.
Great now our mid level objectives now we're going to go into detail a little bit more than we go ahead and collapse everything else that we're not working on you know, we have a High Level we have a mid level let's just walk through this one step at a time writing these spec props you know, should be simple, you should just be thinking through, imagining what you want to see and then thinking about what you would want to communicate to not just the LLM but to yourself if you were writing this or to another engineer if you were writing a plan for them to generate the code for so mid level objectives you want to add a bar pie and line chart capabilities Capabilities in a new char to file add output file functionality to a new output file PY file exactly and let's just keep going down the line here add two new CLI arcs and they're going to be exactly Yep chart and output file to our type method at a mid level.
Right, we're just kind of going in level limb, so we're adding charting, we're just adding a little bit more detail into how we're doing that with our mid level objectives.
So let's go ahead with our implementation notes so any technical details, dependencies, coding standards and just other information.
Right so this is where we can kind of be more specific this is where we can guide our reasoning model.
This is where we can be more prescriptive about minor notes or tweaks that we want our assistant to be aware of.
I'll say Matplotlib for charting exactly be sure the output file uses the correct file extension.
Output file options are Let's see us do a.txt, let's do a JSON, let's do a.markdown and a YAML and then let's go ahead and specify our charts chart types.
Let's go ahead and do exactly up that looks great and anything else we need to mention here in our implementation notes, I'll just say be sure to follow the low level task and order and in detail, so just gathering some more attention to our low level tasks, context is important, so what's the context at the beginning.
So what do we need to run this?
I'll go ahead and drop all existing files just so we can get a full reset here
so we can rethink this
and we're definitely going to want our main
so I'll say you know, beginning file we want main right
and it's going into our full file extension here just to be super legitim about it.
Quick tip for grabbing the file names in VS code If you open up the main PY file, you hit command Shift P and look for Rel so relative you can copy relative path of active file I use this a ton when I'm setting up context for eight or instances so you can copy this
and then we can hop back to this file and just paste
Okay so want this added data types.
So let's just go and paste this again and then modify the file name we want data types.
Let's make sure we also have our Pie project Toml file.
This is Yep that's going to be read only.
We also don't need to make any updates to our data type so we can just go to make that read only as well.
So I think that's it, this is why it's nice to you know, write this top to bottom we can come see
and we can always be reviewing what we're trying to accomplish, you know, as we're thinking about our new charts file
Right A new chart Stop Python file We can think what else do we need to have in the context window to accomplish that task, so that should be good so in the end we're going to have of course, all of our previous files and a couple new files right, so we're going to have chart up PY and we're going to have we call this output format that PY right
and we make sure that I update that here so we're being consistent with our file naming
and so that's our ending context.
We're working through the changes we want, we're adding detail, we're adding context, High Level, objective mid level implementation notes and then contacts and you know, as we're kind of drilling down at the end, we're finally ready for a low level prompts just go ahead and dig into this and let's think about the changes we need made for our low level prompting tasks, so we should only need a few props here, let's go ahead and clear this out, let's think through
this right
so we're going to create our output format so it's going to write that right create source let's go ahead and use some of this auto complete I am running getup co-pilot here for some auto completion help and I'm going to run output format PY so we're going to create this file and what we want in this is our format functions
Right, so we're going to pass in, say, create format as string and I going to pass in our analysis.
Right,
so exactly Yeah we're going to pass in our transcript analysis and in our previous version we only pass this in.
Let's also go ahead and pass in our word counts and we're going to use our word counts type right and in fact we're using both of our type, we have these available in the context window.
This is really important.
You always want to be thinking from your A coding assistants perspective, That's exactly what we're doing here
so we have the data types there and we're also going to specify the return type so we want a string back from this
and that's it.
So when it hit Comma and you know, remember we don't only want a text format, We also want Jason Markdown and YAML, so we'll use our list continuation, prompt pattern and just say format as Jason will drop a lot of the detail because we're just repeating here
right
and we can fall back on the language models.
Great abilities to pick up on patterns, so we're just going to start exactly writing this as a list you can see even co-pilot is picking up on the repetition that we're looking for, so this is great we have all these methods and I think that that completes our first prompt Here go after this runs, we'll have our output format, accepting our transcript analysis and our word counts from our main file,
Right so this is great, so let's go ahead task to this is our charts functionality
so we can go ahead and start writing this out right in this prompt we want to create source spec base
right
and we're doing charts perfect, We want to create what do you want to call this Create bar chart and we're going to pass in Of course, our word counts up so we're getting some nice auto complete there What we want to do is actually add some detail
Right, so it's not just as simple as passing the method because you want to modify the behavior here
so I want to say horizontal bar chart descending top to bottom because I want the higher numbers at the top, lower at The Bottom
and then we want to bring back in that same quartile logic that we had before, so it's really important to dial in when you're writing your prompts, dial into exactly what you want to see in this context and by using this you know, great a coding prompt pattern of locality Rights were saying in this file.
In this function you can start to see how useful it is for dialing into one change at a time, being really specific with the changes that you want to see Karen, so we'll continue here and what we'll say is what else we want, we want our top quartile green bottom quartile short red
and then we'll say remaining blue.
Right kind of just as before and now what we want to do here is we only want to save as Yeah sure save as
PNG g
yeah
this is our bar chart
so it's go ahead and create two additional
so I'll say create pie chart
and I'm going to use the continuation pattern here for our LM to just pick up on
and I'll just say colon mirror, Create bar chart exactly
and then our last one will do the exact same thing so this is great, this is our Churt prompt
so you know oftentimes right when you're writing code, you're instantiating some pattern
and then you're just following that pattern in subsequent lines of code and subsequent files.
So language models and coding assistance, They're really great at picking up on these patterns and the list syntax here and the mirror keyword allows to tap into that idea of patterns.
Right so let's continue that's all information we learned in lesson three we're using information dense keywords to our advantage here let's go ahead and wrap things up.
I've forgotten to write the High Level task here, so let me just go ahead and at a High Level say what's happening so create output format functions and then I'm saying you have to create sharp functions, right, so this is a super High Level void of information.
We're just naming our task effectively, then I'll say update main to use the new functions and let's go ahead and write this last information tense keyword to drive things home you see, we're getting a nice auto complete here from copil this looks actually pretty good
so again I want to emphasize why we set up so many patterns in lesson three and lesson four.
Right, you can see even co-pilot is starting to mirror our behavior in this file and that's what you want, you want to be setting up patterns for use so that every piece of compute, every auto completer, every prompt, every coding assistant they all start to understand the language you're speaking.
Why because your language is consistent, because your language is information rich right you can see it's picking up on similar keywords right, similar information, dense keywords we have update that's exactly right, we have add right chart and output file cl
Orgs That's great
and then we have use output WY functions perfect right use chart WY functions pretty good couple just tweaks here I want to say and write to an extension appropriate file.
I just want to be super clear about that based on arc
great
so when you start setting up these patterns you're starting to speak a reusable language that you know your computer more specifically language models can understand right
and this is the power of consistency it's the power of pattern recognition and it's the power of you know information dense keywords
so you can see everything we're doing here, stacking up, we're speaking the language of, you know, language models, so let's go ahead and fire this off quickly, we'll just review your contact, Make sure this all looks good and make sure that we're being consistent with everything, everything does look great here
so I'll just goad and copy everything and let's add, let's set up our context
right so we want to add name
and then we have two read only files we'll use AER's Read only command to pass in data types and
PY project.toml
Ok so now we have that and you can see our end state is super super clear so the ending context is, you know, very well-known we can go ahead and again we're going to copy everything and paste it into our Ader architect instance using the Owen reasoning model and call the Sonnet as the editor, will it enter and let them do the hard work, it might seem like a disadvantage having to wait for a reasoning model to return but actually helps you think ahead, there's always something else you can be doing to progress your engineering, including writing your you know next specification prompt or you know, setting up your secondary assistant like we can do right now to get ready to iterate on whatever result, our architect and Since gives us
Okay
so we got changes back let's go ahead and just review these changes fairly confident in the result, here I'm going to hit Yes, while our editor agent is making the changes we can review so hit Yes, we'll have our editor start making those changes for us and let's scroll to the top here
Okay, so it is executing things on a task by task level, just like we asked so you can see here create new file We have our format as string with the exact parameters we specified, it's creating that great format for us, right, and it's inferring based on the types that it has access to.
Right it knows what these both look like and it's accessing all the right fields right bullet point highlights sent an analysis, keywords Get format is JSON right, so we have a simple you know, json.dumps call happening here with a new combined set and you can see here our workouts is passing in our workouts dictionary, so let's clean format as marked down Same deal here format as YAML and we do have access to YAML Here our coding assistant can see this because it has access to our Pie project file we can go ahead and open it up and you can see that right here
right so we do have our YAML library
Okay and now our second step so that was all step
one right, all that code was generated from step one if we open up, plan and collapse go to low level tasks and collapse.
All of these are We have three tasks.
The output format was just one prompt and look at what it did, look at how great all these generations were.
Right, this is called scaling your impact, this is called truly tapping in to the abilities of the reasoning models.
This is just one step and it nailed it so let's go ahead to step two now we're creating our chart methods so you can see here we're pulling in Map plot lib, we have our core tile size so we have the top bottom core tile, it's defaulting everything else to blue and looks like we might have some issues here we'll see and let's go and continue so that's our bar chart we also have our pie chart here
and we have our line chart so that's good, that's step two and then step three here pull it all into main add these two new flags and then create our files
right so you can see here if output file we're then writing this so this is interesting so if we look at step three.
Okay we are saying output file flag so I gave it the wrong information here I did just want to pass in an output type, but I did say output file so that's what it gave me.
Right so this is, these are things that will just happen, this is fine to we can specify an output file and then it looks like it's looking at the extension to know which function call that's still great.
I made a mistake there right, so I made a mistake it still completed it insanely well based on my mistake, so that's why we can roll with that and at The Bottom Here we have our chart calls got So this looks great and then we have new usage documentation that's great to see and now we should have our creation statements here by our editor model, which we do.
So let's go ahead and just approve these so there's the output format, there's a chart and then there's our three multiple edits with our edit architect, with our spec document with the reasoning model.
Right so this is really powerful stuff, I really hope you can see what you can do with this.
Right, these techniques can run on any codebase you have any single code base you have, it's all about putting together a great plan and you know, using AER as a powerful code editing tool, right and to be clear, you know, I know we're digging more into eight or specific things, but this architect model pattern is simple you have a draft prompt
and then you have an execution prompt We will definitely see versions of this, variants of this you can imagine a world where you have two editors and then you have a Lead Engineer Thein takes the best of both worlds and then hands it to an editor you can imagine you have an architect and editor and then a reviewer you can imagine you have a architect and editor and then a critique you can imagine you have this workflow run a couple different variants There are many ways to construct prompt chains and a coding agents to generate improved outcomes using a powerful reasoning model and then great base models like CLA Right, so let's go and continue AER is just asking US-A couple extra things here do you want to add some stuff to the chap's going to skip all that clear and let's review our changes so we have chart up
PY
Right so this looks great, we have our bar chart there we have our core tiles, I think the core tile logic might be a little off but that's fine, we'll just gloss over it we have create pie chart, create line chart
and then we have our output formats so we can go and just collapse this
and you can see we have string JSON marked on the ML just as we asked, and then finally in our read me we have a couple new items here and let's just go ahead and copy this
and we do need to again drop the method name so we can just go ahead and drop that or we can keep it and just do this right because basically types just saying there are no other commands to run so we can come in here and just say temp
Ok
so whatever so now we can refer to type or with specific command names.
Okay, so this is great, so let's go in and just run this we have default in counter ten, Let's browse through our code, everything looks fantastic.
Let's go ahead and execute opening up a fresh terminal here, going to paste this in and let's see what we get.
Okay, so we have an error here.
String has no attribute create pie chart so we can just search create pie chart, we have this chart we're saying if chart
and we also imported chart up here so simple issue you can see we just had a important naming conflict.
We're going to open up our base model AER instant and we're just going to quickly resolve this and we're going to hit add, we're going to update main and let's go ahead and add chart as well.
I'm not sure we'll need it, but we'll add it and all we're going to do is come back to this error, copy it and we'll use the resolve keyword to go ahead and knock that error out and these advance Rang models will know exactly what's going on here
so it's going to go ahead and just change the name of that variable.
Right, basically we just had two conflicting variable names so as clean up let's go ahead and rerun and we don't have chart, we now have chart type as was just updated so let's go ahead and update this to type.
If we search for chart type right, this is our new keyword to prevent the chart naming conflicts will enter here
Fantastic
so you can see we have our print, we have our analysis, we have Pytt saved and we have output written to empty so let's go and just take a look at that, let's look at our output and you can see here we're not only getting our transcript analysis, We're also getting all of our word counts in a marked on file looks great and we also have a pie chart here
so you can see we have all of our words split out in a nice distribution, this looks great.
Right, so let's go ahead and run a couple more tests.
Let's create a YAML file as our output and I want to see that bar chart.
I want to see our core tiles come in so we go ahead and run this and let's see what we got so we have our bar chart here and we have our YAML look at the YAML first so this looks great.
Right, I love the YAML formats very readable while maintaining a lot of the you know, JSON object structure nesting and let's look at the bar chart wonderful
so the quartile logic is in there just as we asked.
The top cortal is green, The Bottom is red and the rest is blue.
So there's a lot going on here right, but this is beautiful so that was maybe what one or two follow up prompts with a simple base model and to spec prompts using a reasoning model and the useful architect mode.
Let's go ahead and close and just discuss what this all means and how this is valuable for your AI coding abilities.
I know that this can seem like a lot.
This is one of the techniques in the course that can take some time and effort to understand and use.
It's critically important to take some time to understand and to write out Spec proms, Write this idea of planning your work and then handing that off to a powerful reasoning model.
You want to spend time to understand and use this.
You can also test Architect mode with a variety of models.
You can, for instance, run a clogged 3.5 sonnet as an architect and an editor, and you'll get some pretty great results.
This will somewhat work, but it's important to call up that the reasoning model is particularly effective here for writing large scale spec files that make changes across multiple files.
We're talking 51020 plus files because it iterates and it's looking at your contacts again, it's reviewing things you're asking for in implementation notes, It's reviewing the High Level objective it's looking through your low level prompts over and over reasoning models are particularly advantage to writing and generating massive
and I mean massive amounts of code like I mentioned in both of our spec files here, but if we open these back up our first spec prompt was the largest we're running.
Five individual prompt we're asking for five concrete changes and our second one we only had three changes here, although we generated quite a bit of code in each one of these methods, which is fantastic, Definitely copy the spec template from this course From this codebase I'll also add a link to your loop box Reuse this to generate new micro applications and to generate new features into existing code bases as you use this play with it, modify it at sections, remove sections Remember the key is to create reusable patterns to best communicate with your AI coding assistant and your language model so that you can get more done and hand off more work to them to the model, to the AI coding Assistant.
This structure has worked extremely well for myself and for other engineers, so it's likely to work for you if you use it.
The general flow for this new AI powered development workflow is Write your respect, prompt think through all the changes, fill out the context.
Think about the beginning and the end, go top to bottom here and then work through your low level prompts.
This is where you'll be spending the most time now expect to have to go in after the completion is ready.
For now, as these reasoning models are still improving, expect to have to go back in modify a couple things you know, resolve a couple issues you saw we had to, you know, add our main block back We also had to, you know, fix a naming duplication you know, expect to have to come in and iterate a little bit, it won't be perfect, but in the process as you write more Spec DOCs you'll start to notice something incredible the spec will get you 80% of the way there, then it'll get you 85% then 90 and then as you improve, as you learn how to write these information rich prompts in the right order with the right information, right, with the right context.
Eventually it'll hit 100% and once this happens to you a couple of times you will have a massive ah HA light bulb moment when you write the perfect spec prompt and the LM interprets it perfectly and you make five to 1020 multiple edits all at once.
That's the moment you transform into an engineer of the future and I hope you can see how and why After this lesson, I hope that vision is now clear.
Hope is a clear path to you getting to that place because that's the next step you need to get to that moment where you generate massive amounts of code with the right plan.
Now I recommend you take a break from this course and practice everything we've done so far in lesson six and seven, we're going to once again take everything we've learned and scale it up even further.
We're going to add a new dimension of AI coding that enhances your output across code bases by eliminating entire classes of engineering work entirely.
In our next lesson I'm going to share AER secret and we'll put it into practice to change the way you engineer once again.
Great work here in Lesson five.
Take some time to digest and let your engineering mind shift around this new way of writing code with AI.
Now the plan is the prompt and great planning is great prompting.
I'll see you in less than six.