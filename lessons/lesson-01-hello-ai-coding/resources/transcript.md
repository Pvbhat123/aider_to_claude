Welcome to principled AI coding.
In this lesson you'll step into the world of AI coding and begin your journey to obtain superhuman coding abilities.
We have one mission in this lesson.
Set up your AI tooling and introduce you to fundamental, useful AI coding patterns that you can reuse across code bases across time.
Every lesson contains one key principle that drives the lesson and your first lesson here where Hyper focused on one of the most important design philosophies in software engineering Kiss Keep it simple, stupid, this is one of my all time favorite principles because it's relevant for beginners and seniors, It reminds us not to overthink things, especially when we're learning something new whenever you are learning something new, it can be easy to veer off course, get distracted, feel overwhelmed or confused if you ever feel that way in this lesson or throughout the course remember keep it simple, stupid, even the greatest engineers fall off track, get distracted and hit roadblocks if this happens, if you get distracted If you fall off course Refocus all your attention on the fundamentals will cover right now there's so much information out there, so many things happening, so many decisions to be made.
So many opinions to be heard, but right now all you need to do is focus in on this very moment I've taken all the complexity, all the information, all the decision-making and I've abstracted it away for you all we're doing here is setting up your AI tooling and running your first set of AI coding prompts That's it, Keep it simple all the way through in your first lesson you'll step into the world of AI coding and begin your journey to obtain superhuman coding abilities Now let's get you set up with the essentials I'm going to show the prerequisites on the screen if you're missing any of these, go ahead, pause the video, your loop box below will contain every link you need to get set up, install these and come back when you're ready now let's open up the terminal and validate that you have everything you need to be successful here we're going to run UV version
Perfect We'll run GIT version Perfect Python version Perfect and Pit version perfect Now go ahead and create a directory where we can clone and download the less one
Coase Now it's clone the lesson one code base this is going to be a link in your loop box below.
Now that I've cloned this, I'll type Ls and CD into this code base and now let's install your new AI coding assistant AER.
We're going to use this command to install AER.
Remember every command you see in this video is going to be available in your loop.
Boox below will install AER At the install we can run a version.
This lets you know that you have eight or installed nice work Last but not least, we need a language model to power our AI coding assistant.
In this lesson we'll need an open AI Api key, but I also recommend preparing an anthropic Api key as well.
We're not going to worry too much in this lesson about what model is going to run, we're just here to set up the basics if you need it will have a link below in your Loop boox that will walk you through the process of how to obtain both of these keys.
Remember, do not share your Api keys with anyone.
After you obtain your Api key, you can set them in the command line like this Export Open AI key equals and then go ahead and paste your Api key.
Here I'm going to cut this part out of the video so that I don't leak my Api key to you.
If you have an anthropic key you can go ahead and use This command, of course, is going to be available in your Loop boox below as all of our commands will be.
If you're on Windows, check out the link in your Loop Boox for setting up and exporting your key on a Windows machine.
This course was designed so that you can optionally work with me in parallel.
That's definitely the preferred way you'll get more out of it and you'll understand the concepts in real time, but of course you can sit back, relax and just absorb this information passively as well.
We're almost there.
Let's go ahead and open up your favorite code editor inside this repository.
I'm going to use VS code throughout this course.
It's all just type code.all right, so you can see we have a simple Python application, We're going to be working in our main file here when go ahead and open this up and now it's time to write your first AI coding prompt with a or go ahead and open a terminal inside your repository.
I'm going to use VS codes terminal with the command Jay Hawkey and now if you have everything set up properly, you should be able to type A or you'll likely have a future AER version and you might have a different main model specified the key thing to pay attention to is that you should see something like this get repo with five files I'm going to go ahead and hit control L to clear the command line interface and now we're going to give AER some files to work with.
We're going to type Slash add space main.py Now either can see the main.py file.
I'm going to type control L again.
You'll see me do this quite a bit throughout the course and now we're going to write your first AI coding all we're going to do here is type print
Hello AI Coding world you can see AER automatically made that change.
We now have a print statement here in this file and AER now may be asking you a couple of questions.
It knows that we're operating in Python, so it's asking us if we want to run the shell command, We'll go ahead and type with Y for Y and now you can see AER went ahead and ran the commands you can see our print statement Hello AI Coding world and now A is asking do you want to add the command output to the chat as you write code with AER it's constantly keeping track of everything you've discussed, all the inputs and all the outputs we're just going to go ahead and hit the Yes here now AER can see the command we ran and the output of that command if you made it this far and you ran this congratulations you just wrote code using AI before we dive into the model or additional commands or anything.
Let's remember to keep it simple and just continue to explore what we can do with this.
Let's run some additional AI coding prompts only give you a fundamental understanding of what you can do with your new AI coding tool.
I'll type Control L again.
Let's go ahead and modify this main file with additional AI coding prompts.
Let's run update to print ten times perfect
and then we'll go ahead, we'll say yes, AER wants to know if we want to run the shell command again, we'll go ahead and say yes
and you can see there we now have ten Hello AI Coding World prints We'll add the output to AER's chat window
and then we'll go ahead and clear once more you can see here same deal once again automatically, the code was updated for us.
All we're doing is typing a natural language.
Let's push it further.
We'll say store string in variable and pass into print perfect so same deal we're going to hit yes, yes once again the code was automatically written for us and we have ten Hello AI Coding world and we added that again to Ader's chat window.
I stop.
Let's go ahead and push this further.
When you're writing code with AI at the beginning, we want to keep things simple and focused on making one change at a time to understand the technology at a fundamental level.
Let's go ahead and move this code into a function so we're just going to go ahead literally type that we will say move the print into a function and pass in the variable perfect.
So now we have a message as a variable and now it's getting passed in to a brand new function that we just wrapped and were doing the same thing.
Right printing ten times we'll go ahead and hit yes, we'll hit yes now we're moving now, re making progress.
We haven't written a single line of code and that will be a recurring trend throughout this course.
You and I are very, very rarely going to actually write individual lines of code.
In the age of generative AI there will be fewer and fewer times where you'll actually want to go on and write code yourself unless you're correcting something.
A good sign that you're making progress writing code with AI is that you're not manually obtaining code yourself.
What's clear the terminal so let's go ahead and run one more prompt.
We're going to keep things simple while progressing.
I'll introduce you to one additional command that's really important for managing your mistakes and your assistants, mistakes or software engineers.
This is bound to happen at some point you're going to make a mistake.
The only question is, how quickly can you roll it back and get to the correct solution?
We're going to write this prompt comment out all code and our ecoding system will automatically take care of this for us.
Great so you can see that's all come to up
and now what we're going to do is use this new command Slash Undo, so if we type Slash Undo and hit Enter, you can see there that change just got completely reverted.
It doesn't matter what was in that change.
In future lessons we're going to be updating many many, many files with our A coding assistant.
The/on Do command will literally move you back in time before that specific prompt was rung.
This is a really important command to correct mistakes quickly.
Everyone falls at some point.
The question is, how quickly do you get back up after you've fallen?
Undo is your instant get back up command.
Let's go and clear the terminal again
and so I just want to highlight what you've accomplished here.
This is nothing short of incredible.
Right, I know that this is a super super simple example and if you have experience you're probably glossing over how simple this is, but this is really important.
Right, nothing is more important than the groundwork you lay for yourself, your leveraging natural language to instruct your AI coding assistant, effectively reducing The Gap between your ideas and executable code There are a few things to keep in mind here as you continue your A coding journey as you work with additional files, we're finding your prompts will be crucial to ensuring accuracy and efficiency.
Remember, large language models and a coding assistance are tools to augment your capabilities.
Now replace them.
More than ever.
We are moving to code reviewers and code curators.
Don't be an amateur that doesn't know what they're creating you have to know what you're looking for in order to see it, you have to know the end state that the A coding assistant will get you to at least at a High Level in order to create it.
So how does this work at a High Level?
How do AI coding assistants work at a High Level?
Are AI
Coding Assistant here sits on top of a large language model.
While models will evolve over time, you might be using a next generation model, the core principle and the architecture remains the same.
The large language model is what generates the code for you.
We then add files.
In our example here we have a single main PY file, and files are also known as context.
Right, this is information that your prompts and your A coding assistant can operate on.
This is information that AdR can explicitly read as you progress and write in larger code bases.
This explicit file adding becomes ultra important because Ader reads those files and those files alone.
There's some small copy us of that.
Sometimes Ader will ask you to add additional files if it thinks something is missing based on your prompt, but for 99% of the cases the files you've explicitly added that's what your a coding assistant will be able to see and operate on.
There are some A coding tools that have some magical patterns and some magical auto matching to try to automatically pull in contexts that thinks might be relevant for you.
There are advantages and disadvantages to that.
Lastly, we write a coding prompts that AER passes to the LLM which writes your code.
AER takes the generation, validates it and saves it to your file.
These are the three essential elements of true AI coding assistance, context model and prompt.
These are essential ideas we will discuss in our next lesson multi file editing.
Now that you've written a few AI coding prompts, Let's apply your skills to a practical project building a word frequency counter.
This exercise will put your learning to work and demonstrate the power of AI coding assistance.
The frequency of words in a string gives you a rough estimate of the central theme or topic.
This can be useful for simple yet effective data analysis on presentations of any kind.
You can use this on Youtube, videos, on conference presentations, on work meetings and and really any presentation that can be transcribed into a single block of text you can see here we have this transcript txt file in this starter code base.
This is a transcription from a YouTube video we're going to use this and count the frequency of each word in the script, so we're going to do this in just for a coding prompts In under 1 min I'm going to clear the main file and we'll start the timer as soon as I open AER let's go, I'll type AER I'll add the main file then I'll say read transcript txt and set to VAR Great
I'll skip the outputs
and then I'll say count the frequency of each word using a dict to store counts
great
then I'll say display the word frequencies by printing hashtag for each count
Awesome
and then finally I'll say sort descending before print sweet
I'll stop the time their moment of truth open up a new terminal
and then I'll type Python Main you can see here we have all the words and frequencies for each one of them and if we just go ahead, scroll to the top here we're going to see some larger frequencies showing the number of times the words appear obviously you can see there are common words like and the two of you that are very, very common and if we scroll down you can of course see AI start to pop up you can see file
and then you can see loops, so on and so forth, right, so in just four prompts and under a minute you know we have this really simple working file.
This is just a taste of the potential of what you can do with these AI coding tools.
This is a simple application that can be written in a lot more simplistic ways, but the ease in which you're able to build something like this really needs to be highlighted.
The simplicity of AI coding allows you to focus on the outcome and structure of your program while the AI handles the repetitive lower level details.
AI coding shortens The Gap between what we want to create and it existing.
For example, we can make a couple quick tweaks to this program to make it a lot more useful.
Let's say we only want to display words that show up more than three times and let's say we also want to have the total printed alongside the word.
We can literally just open up eer, add the file again and then just type nearly exactly what we just said, only show words with count greater than three use a variable and then we'll use a period here to denote that we want multiple changes.
This is a small thing that adds up over time and then we'll say after word before hash, tag show the total for the word Corre and it'll just kick that off so we'll be able to watch the code getting written here in real time.
You can see we have the min count threshold and then we have the loop now running at The Bottom here, so let's go ahead, exit or here and type pathon main or you can go ahead and just use a or to kick this off it will enter and you can see here now now we're only seeing words here that have three or more occurrences and we also have the total between the word and the hashtag There are many ways to tweak and improve this, of course we might want to filter out a lot of these common words so this is awesome, right, really simple program lots more we can do here tons of ways we can improve, but now you have a great groundwork for what's coming next as you continue to develop your A coding skills, you'll find that a coding can significantly speed up your development workflow, allowing you to tackle more complex projects with ease.
So what's next?
You now have the basics and the fundamentals.
You can start to see how this tool can give you superhuman coding abilities, and our next lessons will build upon what we've learned here and explore multiple editing and context management.
This will enable you to manage real coding projects effectively.
Will also learn additional commands to better manage your AI coding sessions.
If we open air and type slash, you'll notice a large list of commands we're going to cover and focus on the commands that matter the most for your AI coding journey, we're going to learn the most important commands one by one.
Incrementally, we'll learn how to add additional files, remove files, change the language model and track your token usage so that you can monitor your costs using these tools.
Just a quick note on pricing and tokens your time is worth a lot more than a few bucks here or there.
I definitely recommend you eat the cost and use of the higher quality state of the art models, so let's quick review what we've done here.
Right we set up our a coding assistant Hter we kept things super simple, We just focused on getting value out of your A coding assistant, We ran Basic A coding prompts to break the ice and then we built a small transcript Analytics application in less than a minute and we did it by keeping things simple and focused on the core value that AI coding tools offer you rapid natural language code generation This is AI coding you are AI coding That's what this lesson was about and you made it to the end here.
Great job Keep the Kiss Principal as your guiding star.
As we work through upcoming lessons, things will get more complex.
We're going to be doing more with their a grating proms, We're going to be using complex reasoning models that are able to generate 510 plus files for us with a single prompt.
We're going to be refactoring large swaths of code, we're going to be creating, reading, updating and deleting multiple files, we're going to be working through more complex commands, powerful AI coding patterns and brand new ways to write code in the age of generative AI throughout all of it.
Remember this lesson, remember the core of what's happening here.
Rapid natural language co generation Keep the kiss principle close to you as your guiding star.
As we work through these lessons together, focus on keeping your AI coding prompts simple, direct and focused to better harness the full power of AI coding.
If you write a prompt that you don't understand how to turn into running code, double-check your prompt adm more detail and makes you know what you're trying to generate, makes you know the outcome you're looking for, I'll see you in the next lesson where will dive into multi file editing to expand your AI coding capabilities, Check your Loop Boox to see everything you've unlocked by watching this lesson, I recommend you walk through everything we've done here and power up for what's coming next.
Great work here
and I'll see you in the next lesson, or will dive into multi file editing to push your AI coding capabilities to the next level.