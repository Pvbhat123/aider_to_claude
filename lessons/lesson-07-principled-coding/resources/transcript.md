Welcome to principled AI Coding Lesson seven In this lesson we accelerate on the parabolic curve of AI coding.
This is the lesson where your abilities can multiply far into the sky.
In this lesson we travel into the dark hole and peer into the future of AI coding.
I'll say this up front, this will be the most controversial lesson of the course because here we can start to see the edge of software engineering and it's unclear what's beyond the edge let's dive right into the principle for this lesson.
In this lesson we close the loop and we let the code write itself.
What does that mean and how is it possible?
And this lesson we push into the implication of AERs secret.
The fact that AER is programmable and scriptable means that you can build agentic workflows that solve coding problems for you.
Once again, the only question is can you align the Big Three context model and prompt to give your AI coding assistant what it needs to accomplish your tasks.
The Big Three bulls, eye, just like our other principles, remains just as important, if not more important, as you scale up your AI coding abilities Every lesson, every principle builds on each other and they become more important the more you're pushing your AI coding abilities in this lesson we add the idea of closing the loop as the next principle on top of everything you've learned so far, so what does this principle look like in practice, let me introduce you to the director pattern also known as the director loop, This is an agentic workflow where you define your context, prompt and model as usual and then you define an execution command and an evaluator.
These are the two missing pieces you need to close the loop.
Your execution command runs after your AI coding assistant has generated your code and then your evaluator takes the output of your execution command and determines if your task is done.
If your task is not completed, it creates feedback and then loops back in to your AI coding system, Closing the loop an evaluator can be a piece of code, but we're going to focus on evaluators that are themselves large language model calls This is a pattern from language model testing you may have heard called LM as a judge where you have an LLM grade the output of another LLM
With this pattern we close the loop because now you can write a prompt Have your AI coding Assistant generate code Execute the code, evaluate the code and if the evaluation fails, pass the feedback back into the AI coding a system This pattern is the prototype to the future of AI coding the future will we let the code write itself by building upon patterns we've established and the AI developer Workflow and the Spec prompt In this lesson we close the loop by giving our AI coding assistant feedback through an evaluator function with this pattern, even in its early form we are approaching the edge of AI coding and potentially the edge of software engineering as we know it, This pattern enables AI coding tools to act in a more autonomous way solving your problem iteratively until it's complete.
Next generation AI coding tools like Devon and Github's co-pilot Workspace rely on patterns like the Director pattern to run autonomously.
Now let's come back to Earth and walk through a concrete example of how we can close the loop and let the code write itself.
Let's open the principled AI coding directory.
If we type Ls you can see our previous six code bases.
Let's get clone.
The lesson seven code base link will be in your loop.
Boox.
As always, I'll CDN to our Pack Seven codebase and Open vs code right away.
I'm going to drag my.environment variable file from my previous code base into the directory.
Now I have access to Open AI and Anthropics Api keys.
Let's open the read me, open a terminal and let's get started.
I recommend you set up both the Open AI key in your.environment variable file and theanthropic key we're going to be using both throughout this lesson.
Let's run UV Sync to install our dependencies and just for good measure, will run UV run Main to make sure our application is working perfectly, will be building off the latest version of our Transcript Analytics application to understand this new director pattern we have our output as expected and inside the read me
you'll notice we have a new command here where UV run Python Director PY with this config flag past in let's go ahead and open up this director configuration file and break down the director pattern so we have a new YAML file format here, but you'll notice key value pairs you've already seen at the top of the file we have a prompt filled with information, dense keywords because we have update keywords, create keywords, add file references, function references and all we're doing here is building out a brand New Green themed HTML base file output We update the output format We update our main file and most importantly, we're updating a test, so we have our prompt
and then we have our model, you can see here our coder model is defined to be the Clawd 3.5 Iku model you can update this to be any A or compatible model you like and then we have our context, we have editable context and read only context you can see this is set up much like our Adws, our AI developer workflows and then we have the magic of it all, the execution command and the evaluator you can see the execution command is a UV Run PY Test command We're running all of our tests and we're disabling warnings, So this is going to be really important.
We're going to circle back to this we're going to quite literally circle back to this in our code Below this we have our Max iterations so our A coding director loop will only run five times at most.
We have our evaluator model set as GPT for O
and then we're running our default evaluator method.
As you build up the director pattern, you'll want to build out.
Different evaluators will set this as default and explain what's happening here in just a moment.
That's our director configuration file.
Now let's go ahead and open up the Director Python file.
You can see this is right on the top level of the code base.
I'll collapse everything to the first level and let's walk through this file so at the top we have our evaluation result.
This is what our evaluator method is going to return.
It's either going to be success, true or false and then if false we're going to have, we're going to have a piece of feedback as a string.
Next we have our director configuration.
This is all the fields we just saw from our director file here you can see for our evaluator models, we can choose any one of the Gptt for O models as well as the Oh one reasoning models.
By the time you're taking this course the Oh one model may have fully been released so you can add that here if it's available and then we have the director class, I'm going to open this up and then will collapse down to level two, so we'll fold our code to level two
so we can see the key director methods.
So here we can see at a High Level everything the director does, we can walk through this process top to bottom.
First we create a new AI coding prompt.
We then pass the prompt off to AER and AER will generate the code we're looking for based on our Big Three.
Then we execute our execution command and remember that's our Pie test call here.
So at this point in the code we are going to execute code, right, we're actually running code after our AI has generated code for us, we're going to execute that newly generated code and then we're going to evaluate the result just by looking at the function stub you can see that the evaluator takes the execution output as a parameter and the returns the evaluation result which we saw up here.
Success and feedback.
Finally we have the direct method and this is how we kick it all off.
Let's open this up and take a look of what this looks like so just as described, we have this loop that runs up to five times based on our Max iterations variable, and if we open this up we can see the director pattern top to bottom First we generate a prompt We then run that code with, then execute our execution command with then take the result of our execution and run our evaluate method on it
and then our evaluation either returns true or false if success, we break the loop, the work is done If false, we need to run again, we need to restart the loop and let the code write itself in this loop.
Here we continue to the next iteration and the evaluation.
If we just go ahead and search this, you can see the evaluation gets passed in to our create new AI coding prompt, thus closing the loop.
So before we move forward and dig into any additional details here, let's just close this and let's fire off this director pattern, so there's going to generate a green theme
HTML output type we're going to trigger with HTML G
and then it's going to write a test for us and this is the most important part why, because our execution command will then run this test and if it fails, it's going to pass the failure back into our a coding assistant.
Okay this is a really simple prompt, There is really nothing to be seen here, but I just want to run this through and I wanted to use this as an example to introduce the director pattern to you, so watch the output here
so you can see iteration one out of five create new prompt generating a code.
So now AER is running, AER has taken over and we are running the Haiku model and you can see here just as before, you know, nothing new happening here.
This is our AI coding assistant running with our prompt that we've passed in with the given model and the context, so we're going to get a green themed HTML output file Here you can see our main file got updated and finally our output format test was updated and now here at the end you're going to see our test get executed you can see executing code, evaluating results and now we've reported success, so our director loop with our AI coding Assistant, our execution command and our evaluation has reported success.
Right so this is really interesting obviously this is a simple example
right we're running three information dense keyword prompts so there's not a lot of room for error here, as you'll see in the next example this loop is very, very powerful when we give our a coding assistant all the information it needs and let it run in a loop with legitimate feedback, It can solve some pretty heavy problems, but it's all based on on our execution command and how we have our evaluator method set up so as an engineer it's always good to be skeptical of technology or tools or patterns so you can execute this yourself, you can copy UV run PY test and literally just run what was just executed you can see all of our test pass we can open up output format we can see our New Green theme format That's wonderful now we can go ahead, open up our Read me copy this run example and instead of running a YAML file, we can update this to a HTML G file
Right, because that's how we described how to generate our new format here.
Right, if I just search HTML G globally you can see Main has a new else if block looking for a.html g
so this is great we can go ahead, kick this off and our test pass we know that this structure of code works so we can be very confident that this will execute properly.
We can see we got the output transcript let's open that up you can see here we have some green colors in our style.
Let's open up HTML preview and see the results.
So wonderful.
Right, we have a green themed HTML file format for our transcript Analytics application Fantastic we have some really nice styling here, we got these nice
you know side borders really nice iteration here from our AI coding Assistant
This shows off the kind of point blank capability here.
Right, you can kind of see where this is going, you can see what's going to happen next when we throw a harder task at the director pattern at this a gentic workflow
Right, let's kick things up a notch.
Let's move on to a more difficult example.
Let's open up the slider Director slider output file so you can see here in our specs file we have two director files, one director template that you can use to, you know, use this pattern and build off the pattern
and then we have two spec files right, very importantly here you'll see in the director slide and we close these other files here you'll see in this director configuration file instead of a full prompt instead of writing the prompt here
we're actually passing a spec prompt
so let's go ahead and open this up
and I actually need to update the name of this I need to update to Spec Underscore feature Let's go and save that.
Okay.
So now that should be this file perfect and you'll see what you've seen before here.
Right, we covered this in lesson six, we have a Speck prompt that contained the specifications for a brand new feature that we're building, so we have the header here we have the High Level objective We're creating a new interactive HTML output format with a dynamic word frequency visualization
So we want a slider which allows us to, you know, filter in and out of word frequencies.
We're also going to add to new visualizations for a word frequencies help us injust the information and then of course you know, as before we have our implementation notes, context and, most importantly, our low level tasks which contain some high-quality prompts using techniques we covered and lessons one through four.
So so just to wrap the configuration file, we have the prompt, we have the model and of course we have our configuration, so this gives our a coding assistant it gives the director pattern Everything it needs to execute on this code.
Remember great planning is great prompting we're setting up all of our a tooling for success, but we're really doing is embedding how we ourselves the engineer would solve this problem.
Right, so let's go and keep moving here
so we have the contacts and then we have our execution command, So once again we're just using PY test.
It's important to call out this could be anything, so if we wanted to, This could be running our main transcript Analytics application with this new chart type, right, so we would say something like this chart type and then you know we would expect something like radio, but what we're doing here instead is making sure that in our Spec Prom we're saying you need to create tests for this because we're going to run those tests to determine if you were successful, that's what our execution command is doing here.
Okay we have our Max iterations and then here's something really cool
We're using ao1 reasoning model to determine if we were successful and I want to run this first
and then we can dig into what our evaluation method actually looks like.
I really want to focus here on the High Level pattern of the director loop and not the actual details until further on.
In this lesson, the key here is in the pattern.
Before we execute this, I'm going to roll back previous changes.
We don't need these mucking up the set of application If you open up the AI code block here I'm running with auto commits off, so it or did not commit anything for us, I'm going to go ahead and roll these back
I'm going to run, get restore
and then source so everything under source I want to reset
and then I'm going to just remove our output HTML that doesn't really matter.
I'm just going to remove it for now, so everything here looks good.
Let's go ahead and fire off the director pattern so open the Read me, copy this command and before we run it of course all clear this, get a reference to this file and run the director slider instead.
Here we go so let's let's walk this through and we're going to see something really really cool happen here we're going to watch our code right itself, so iteration one out of five we're now starting to run through the prompt.
Okay we're going to get format as a SML W slider filter
Okay.
So we should get some JavaScript at some point here getting generated, there's a table and there's some script, right, so there's our JavaScript slider wonderful and now Haiku has stopped.
It didn't finish the job.
It's asking us if we wanted to proceed.
Some models do this.
Our evaluator just ran and it caught that right, it said we're not done right.
The test passed, however, the new test for the ACL slider and the new chart visualizations are missing, so our evaluator, although our test passed our evaluator said no you're not done based on the prompt based on all the information passed in you're not done, Run another iteration so you can see here iteration two out of five and now our AI coding assistant is based on the feedback and original instructions I'll focus on adding comprehensive tests and implementing the new chart visualizations and Hl Slider Here we go so now it's taking the feedback and that's continuing.
So create line chart there it is create radial bar chart.
Right we have our bubble chart there fantastic here's our chart tests, Our chart tests are getting updated here, there and then our main file is getting updated.
You can see here we have the new radio and bubble coming in here fantastic, we're getting a summarization and then look at this we have a error here
so we've got a parsing error for the Oh one model that's fine, it's going to fall back on our Four O model.
This happens sometimes and our For O model here now is running evaluation and it's saying almost most tests have passed, but one critical test has failed.
You can see there's a Met PLA live error we got to unexpected keyword
I'm actually not even sure what exactly is going on here, but that kind of highlights the point.
I don't really need to know what's going on.
Our evaluator LM call is going to direct RAA coding system to solve the problem.
Right I'll modify to use plot subplots
Okay.
So we have that update, we have this test running everything passed.
However, the tests for the HTML output format with Slider was not added.
So again our evaluator caught something that was just missed, you know, Haiku just completely missed adding a test for this so it's running the fourth iteration here.
Okay without us doing anything.
Right I, we have, I haven't done anything and now we can scroll here, we can see that that new test was added form an HTML with slider filter and we can see here we got a lynching issue here at or caught that automatically got fixed and here we are four iterations later breaking out of the loop, our director pattern, our AI agents and the evaluator just had four conversations about what went wrong and how to improve it
Okay, let's just take a moment and you know, internalize how incredible that is incredible, that was right.
The code is writing itself and I know you're thinking of a million caveats and what IFS and situations where this won't work and you know you saw the Oh one mini model bomb there on the parsing
Yes, yes, yes, there are many issues with this loop there are many ways to improve this there's lots to be desired, but it is the pattern that is important here and is the principle behind the pattern that is even more important, we are closing the loop with just 300 lines of code, not compact code, not the cleanest code, not the most concise code, but in just 300 lines of code we have an a Gentic AI coding workflow that runs code based on a great plan that we have been building up the knowledge and the skill to know how to build and then we're handing off the coding process to our director pattern to our AI coding assistant to our small AI agent team here.
Okay, so absolutely incredible stuff here before we jump to the details of the Create new a coding prompt execute and evaluate Let's just run this code.
Remember, we are becoming curators of code, we're becoming curators of workflows and we're becoming lean engineers, engineering managers, we're moving ourselves up the stack and we're handing off the low level lines of code the details, the how we're handing that all off to our a coding assistant and our director, loop more and more and more Okay, so let's just go ahead, do a sanity check.
We're just going to run all of our tests.
You can see everything pass as you use this pattern, you're just going to start trusting the system a lot more.
The tests ran that's the evaluation command that we set up.
Here we are using a more powerful O one reasoning model.
This means that we're going to have a more reliable output when this executes and when we get our evaluations and by the way, while you're running this everything is getting logged here to the director logged.txt file so if you scroll down here you can see what everything looks like exactly so you can see the outputs you can see the test execution there passing great
we can scroll up we can see these are all of our editable files and this kind of smashed JSON format you can see our prompt and you know you can really dig in if you want to in this log file here, but so we have this one model, let's go to the read me and let's go ahead and execute some of this.
Right, let's make sure that our code did what we wanted to write.
This was a you know, let's just not forget here this spec prompt is fairly sizable, Right, we have a decent size context, not a large context five files is not large by any means, but you know medium sized and we have a quite a few requests here and you saw Haiku kind of doing one thing at a time, taking breaks, asking if you wanted to do more.
Other models may or may not do that, they might not stop.
Other models will definitely stop and do a more iterative task flow.
That doesn't matter.
Our director pattern took care of that for us.
At The Bottom.
Here we have our four prompts right or for a coding prompts and these are not trivial by any, any means and test for here we're having it in for a lot of information, right, add these tests, these are you know, mid to High Level prompts here in our, especially in this last prompt right, but let's go ahead and execute this because we want to know that it's working, we are still validators and we are still kind of you know, managers of the output of our A coding assistance so let's go ahead and let's go ahead and try the slider first
so I think we're doing HTML
SLD Did I read that right SLD there we go.
Yeah.
So our new extension output to trigger this file format is HTML SLD, which stands for Slider.
Let's go and kick this off and let's see the output of this so that executed pretty quickly Hml SLD not supported, so let's go and see what's going on there in our main file.
It is very possible that our AI coding assistant did miss this.
Yeah.
So our assistant missed this, the model missed this, that's
Okay we can open up an AD HOC at or instance we can add name so we can just come in here, copy this previous command.
Another advantage of writing out your prompts and inspect prompt is that they're always going to be there so we can just copy this and then all paste this in and say only be sure to add, not overwrite
Yeah I'll just buy that off and now let's see what we get here perfect, let's open up main and see if they got added great so now we have this Hml LD you know as you're working through these patterns you can always, always, always fall back on just opening up a coding instance.
In fact, as you're starting to use these patterns, you should expect to come in, clean up a couple things and then run our HTML LD function, Our main is now picking that up.
Notice if we had a actual task running the analyzed transcript, our execution command and our evaluator method would have picked up on that error.
So just want to call that out.
Testing is an important mechanism for execution evaluation feedback, but also whatever execution command you're running should represent the full state of your application as much as possible.
Okay so that output a great let's go ahead and open up this file.
Let's go into HTML mode here HTML preview fantastic
and so you can see here we have a slider at the top we have a kind of you know,
straightforward HTML file
Okay
and if we scroll this you can see something really cool happening.
Our JavaScript is executing and our table is getting filtered right so really cool obviously this happened with a single prompt no styling here
so it's just you know, raw GML and Js really cool to see this come through with the director pattern and that worked, let's dial this back, let's close this and let's go ahead and take a quick look at how the insides of the director pattern look most importantly, I want to show you how the execution command feeds results into the evaluator and I want to show you what prompt we're running for the evaluator model because as I said in the beginning we're using an LM as a judge, This is what makes us an identic workflow you know, also known as a prompt chain or you know a type of chain of thought and really an AI agent.
Right, it's when you start combining LM calls together for a specific use case, that's what really makes this an agentic works, so let's go and just take a look at that we can see this in the director pattern, So if we just open up direct
and we can walk through so we start out with a default empty evaluation If we open up, Create new AI coding prompt you'll see something really interesting if iterations equals zero,
So if we are on our first run, We just want to run our base prompt and in the case of our director Slider The base prompt Is this entire spec prompt file Right, so we're passing that in if iteration is zero if it's not zero.
We take the evaluation from our evaluator method and we run this prompt generate the next iteration of code to achieve the users desired result based on their original instructions.
Okay, so here we're building the prompt to say hey here's what we wanted, where we have the base input prompt here's the output and here's the feedback
Okay, here we're building up a new, a coding prompt when we have an evaluation and will only have an evaluation if we needed to run more than once.
Right, you can see we have a feedback output base prompt and then we're letting our assistant know
hey you have this many tries left
Okay, so that's that we then have our AI code we're taking that prompt that was just built
and we're passing it to AI code An AI code, of course, is just a light weight wrapper around the MVP of it all the most important piece of this our AI coding assistant and you can see here we have our edible context, We have a read only context, A couple configuration variables our model and of course our prompt all right, so just a classic A or call this is the keystone of this pattern, the fact that we can use a high-quality AI coding assistant that's programmable is what makes this all possible again.
This is why I've chosen Aa for this course.
It's foundational, it's open source, it's free minus the model costs.
This gives you control of everything.
It's so controllable that you can write your own AI coding workflows, your own AI coding tools and full on AI coding assistance using AER.
You can see here we're taking it and in a really simple fashion and just 300 lines of code, we're building a director pattern which closes the loop on AI coding.
Okay, so that's the AI code method.
Let's continue here so AER will run and have the side effect of updating the files in its context window.
Okay, we then run our execute method and if we happen to execute we can see here we are just running whatever our execution command was, and if we go to our Director Config file you can see we have UV run PY test We're running all of our tests, we're disabling warnings.
Okay, really simple, really straightforward.
We're writing that to our log file and they were returning both the out and the errors if any exists.
Okay, that's our execute.
And then we have another keystone of the director pattern we have the evaluator method.
Let's hop in here and dissect this.
The evaluator method is building our files so as creating key value pairs between the path to our files and the actual text to our files, and then we have the second most important part next door a coding system We have our evaluation prompt, Our evaluation prompt is what guides the success or failure of our execution.
You can see how this prompt works by looking at a couple things you can see that we return the evaluation result, so this really dictates what needs to happen.
Market success market failed and then give feedback if failed.
You can see we have a checklist you can come in here, you can update this, you can make this anything you need to right the point of these patterns, The point of these ideas.
The point of these principles is for you to take it and make it match your use case, your code basis and your workflows.
We have the user's desired results, so this is our entire base.
Prompt and remember, in the case of our Director slider configuration file, This is going to be our entire marked on spec prompt file, Right, so that's our prompt.
We're then passing in our edible only files read only files our execution command so that this prompt call is aware of what we were trying to achieve.
Right so we need both the execution command and the execution output to make that happen.
Okay and then at The Bottom here we're just doing some JSON string parsing stuff, we want to make sure that it's 100% JSON parsable.
This is how we're communicating to the LLM so that we, you know, make sure that it's returning Jason and you saw this fail
and I think our second or third iteration
and we have a try catch for that reason, the catch falls back to a GPT For O model with structured outputs, Don't worry about these details too much if they don't make sense.
Basically we're running a fallback prompt to parse the result exactly.
If this fails, Okay, but if it doesn't fail, we run its completion and then we run a pedantic parsing method to load our evaluation result from the prompt.
Okay and again all this is doing is saying hey here was the state of the application, right, here's the prompt care files that we were editing and reading, Here's the execution command Here's our execution output Now tell me did we complete the goal?
Did our AI coding assistant do the job it needed to
Right we take the evaluation, we check success or failed right, so this is it right here?
This is it successor fail and if it fails our evaluation is now set for the next loop.
So we have our evaluation here and it runs right in to the new prompt and just like we saw in the beginning, create new a coding prompt takes the evaluation and it takes the index in which we're running on and builds a new prompt for the A coding assistant based on what we need to accomplish next.
So this director pattern, this agentic workflow, this small team of two, this package of code wrapping around LLM's This is a fullon a agent that solves the problem of closing the loop on AI coding workflows.
Let's come up from this and let's discuss the implications capabilities and limitations of this pattern.
We're engineers, we have to face reality, we have to be real about everything that we're building and the capabilities of all of our tools.
The director pattern is an advanced AI coding technique.
It's in less than seven For a reason it builds on AER Secret
The fact that AER is a programmable AI coding assistant, The director pattern requires a deep understanding of your code as well as the expertise needed to plan out work in advance.
The Spec documents, the A developer workflows None of this matters if you can't plan out a feature from end to end, or at least a good chunk of a feature.
I don't expect many engineers taking this course to fully utilize the capabilities of the director pattern.
That is just my expectations.
I would love to be proved wrong.
I would love for you to take this, roll it into a couple of your code bases and really get insane value out of this.
In less than eight you'll see additional use cases of the director pattern really showing off its capabilities, it really enables you to hand off the hard work to your AI coding assistant
and when you learn when to use the director pattern you'll find how powerful this can be.
Future a coding tools will embed this pattern or patterns like this.
What we're saying here is here's what I want done right in a great detailed plan.
Let's go and open up the spec prompt again, you know, there's a lot of detail here, we're asking for a lot and we should be as models progress, as tools progress, a coding assistants will be able to do more with powerful models, so we want to push our spec prompts to limit a massive side effect of models improving and tools like A or existing
is that we can plan much more work than we think, especially with next generation models specifically reasoning models.
Okay, so just want to call that out.
Using a more powerful model will let you do even more using a one preview, for instance, and the evaluation will catch even more things.
So what are the other implications of the director pattern of a pattern where the code Sees the output of itself?
This pattern hints at the future of a coding.
It means that engineers that understand what they want to accomplish from start to finish can hand off nearly the entire process to a self directed AI coding assistant.
It means planning is the key to great engineering.
It means knowing how to evaluate what you can do is another key to great engineering.
It means writing high-quality A coding prompts, Gathering the right context and selecting the right models are foundational a coding skills as we know through the lessons in this course, the implications of this pattern and this spec prompt and a DWS means that you can now wield a coding assistance like never before, It means you can close the loop and let the code write itself, take these principles, take these patterns, take these techniques and AI code like never before in lesson eight, The final principled AI coding lesson I'm sad to say we close the loop on this course, but we go out with a really important impactful lesson you'll see whenever you're ready for lesson eight
So this pattern, of course, has limitations, as you've noticed throughout the course the biggest limitation here is us
and I'm not trying to be gimmicky, I really mean that this is not an end all, be all solution This is an instance of a true working example of an agentic a coding assistant that runs a simple yet powerful closed loop working generic code based on your big three then it executes the code, evaluates the result and then improve if needed the pattern is the value the pattern here is what matters if we open up the director.
There are many ways that this can go wrong.
There are many cases it doesn't cover, but what it does here is absolutely serves as a 80% starting point for using the director pattern and building out a more comprehensive version of the director pattern in your code basis, as you know, every code base is different, there's always a little tweak something, a little different this flag needs to be here, that flag needs to be there, you need to run this set of command First Yada Yada Yada
The director pattern does need to be fine tuned, definitely more than any pattern we've covered because we're not just generating code now right, we are closing the loop we're running the execution command, We're looking for output and then we're taking that output, running it against a powerful model, reasoning models will be the best at this and we're having the reasoning model evaluate the result given the state of the execution, the tooling we're using is in a small, isolated use case of this pattern.
Right, this is just a starting place you'll see a coding assistants adopt, transform and build on this pattern in different but similar ways.
The largest limitation of this pattern is that if your execution command does not provide feedback output, This pattern will not work, so in addition to writing, you're prompt planning out your big Three the task is now on you to create solid feedback for your AI coding assistant and this is a good tell if you should be using the director pattern on one of your tasks.
Can you create a closed feedback loop for your AI coding assistant if you can, if you can run a Seeli command like this or if you can run some workflow where you write some UI and then run a vision agent on the result to evaluate the response or if you can generate a file that the execution command can then validate exists and maybe look at the content of it, then you should be using the director pattern.
Right, this is a, it's a limitation, but it's also just the reality of engineering in a lot of ways what we're doing here is we're giving the AI coding assistant and we're giving our AI tooling the ability to do what we would do as engineers we would go ahead and do something like this I would run this test you know, UV run main and just run the application.
Think about how you can write that into the director pattern.
Right let the code write itself by giving it the right execution command and then by building out the right evaluation method.
We saw here our evaluator prompt looks like this and of course the link for this code base of all this is going to be in your loop boox
you have full visibility into what this looks like you can take this, you can tweak it, you can evaluate the result in many, many different ways I'm confident there's a better prop for this, but this prompt is us 80% of the results again just to summarize the largest limitation for the director pattern is needing access to an execution command.
Right, we need something to evaluate the success of your A coding prompt against and this is why usually, if you're going for the director pattern, you want to use it with a spec prompt right with a huge set of changes with an entire feature kind of dialed in to the spec prompt detailed out because then your AI coding assistant using the director pattern can have a concrete evaluation command and then a great evaluator model and a great evaluator to run and integrate on the results.
The biggest thing I want to highlight once again.
Great planning is great prompting you can see that we can now close the loop and let the code write itself, but it's not useful and it's not efficient if you don't write great plans packed with information, dense, keyword prompts This is going to be a continuing trend in the age of dinner of AI Those who can write more plans?
Those who can write clearly those who can, you know, translate their thoughts into a LM compatible format like the Spec prompt will receive asymmetric results, I hope this principle is clear to you in the age of Jennita Bayi Great planning is great prompting and great prompting enables you to attain asymmetric results before any one else as you will see in the next lesson the things I can do with these AI coding techniques, they're not rivaled right now I'm just going to be point blank
This is not me being cocky, it's not me trying to put any other engineer down there's just not rivaled, I don't see it anywhere and trust me, I've looked I don't see the patterns I'm using anywhere in a meaningful capacity and trust me, I have looked so this is true for all AI coding tools and truly for all AI tooling, Next Generation Models and raising models in particular will multiply your planning abilities with every release, so get your reps in Now the director pattern is the natural evolution of the work we've been doing Spec prompts great prompting, clear, prompting managing your Big Three scripting with your A coding assistant writing Larger code Changes in aspect prompt writing out a developer workflows that completely automate repeat work and now you can close the loop and let the code write itself Congratulations you have made it to the end of lesson seven This is a large lesson to choo if you're really thinking through the implications and the capabilities of the director pattern Yes, it requires more up front investment and requires you to think through how you will execute and evaluate your code on a per code basis, per feature basis, but as you'll see in our final lesson when you put this all together with every principle and every technique we've discussed your AI coding productivity will be unrivalled.
Take these ideas, take these principles, put them into practice and multiply your productivity far into the sky.
If you're just watching, I highly recommend run the director pattern so you can feel the results.
Clone this code base, run the second director configure we were looking at.
Understand the Spec prompt, understand ADWs AI developer workflows and understand that the director pattern are all a reality for you.
Now these are techniques you can use today.
Right now, the most important thing you can do is start get your reps In practice these patterns you want to feel your engineering shift from the how to the what and internalize the fact that great planning is now great, prompting lastly if you're ready close the loop, Let the code write itself, take the director pattern, Make it your own fine tune it, tweak it to fit into your code bases that you're in on a daily basis.
Now you should be writing director configuration files with prompts and then just executing that, increasing the Max iterations, the more you see that you need them and the more that you can see your a coding assistant getting real work done inside the director pattern, Give your a coding assistant feedback by running the command you would to understand if you wrote the code properly, then create an evaluator that decides if the output is correct or if feedback is needed then structure feedback for your AI coding assistant to loop on once you see this, once you run the director pattern you'll see the future of engineering to day in our last lesson we stop, we put together everything we've learned great work here and I'll see you in the final principled AI coding lesson