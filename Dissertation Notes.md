# Dissertation Outline
## Title
????
A look at current business approaches to malware detection and potential inefficiencies in methodologies  
A stark look at theoretical future security loopholes using next generation technology and techniques  

## Content outline 
- [Dissertation Outline](#dissertation-outline)
  - [Title](#title)
  - [Content outline](#content-outline)
  - [Abstract outline](#abstract-outline)
  - [Ethics considerations](#ethics-considerations)
- [Main body](#main-body)
  - [Outline of Preventative Security currently taken](#outline-of-preventative-security-currently-taken)
  - [Outline active detection methods](#outline-active-detection-methods)
  - [Current Malware writing methodologies](#current-malware-writing-methodologies)
  - [Theorise holes in above systems/methodology](#theorise-holes-in-above-systemsmethodology)
  - [Present possible next-generation malware](#present-possible-next-generation-malware)
  - [Show proof of concept in full or in part](#show-proof-of-concept-in-full-or-in-part)
    - [Idea 1. Malware is resistant to forensics](#idea-1-malware-is-resistant-to-forensics)
    - [Idea 2. Malware that is learning](#idea-2-malware-that-is-learning)
    - [Idea 3. A worm can find malware](#idea-3-a-worm-can-find-malware)
    - [Evaluate my effort and other possible avenues](#evaluate-my-effort-and-other-possible-avenues)
  - [ADVISER HELP PLEASE!!](#adviser-help-please)
  - [Advisers feedback/ideas section](#advisers-feedbackideas-section)
  - [Ideas space](#ideas-space)

## Abstract outline  
The idea is to look at current malware defences and what potential future malware might look like with current technology trajectories. This will require a deep look into current security methodologies to prevent malware infection. Because the subject is so broad however, I will look at worms over other types of malware, as worms are the most weaponised and most impactful types of malware. 

## Ethics considerations 
Any malware I create is ethically questionable generally, as malware inherently is a thing designed to do harm. Therefore I must take extra steps to ensure that whatever I write does not become the next leaked malware to cause havoc on the NHS. Firstly, I think that I will develop the entire thing in python. This means that because it's developed in an interpreted language it would have to be completely rewritten in another language to be widely effective. If directly compiled into C code too, it would have all the markers and inefficiencies that come with converting python code into C. I think that all steps should be taken to use out of date methodologies and payloads in the code sample too that are outside my specific proof. If I limit my proof of concept to a solid outcome then it should be possible to create a sanitised test environment that would be exploitable in the lab but never seen in the wild.

# Main body 
## Outline of Preventative Security currently taken 
## Outline active detection methods 
A lot of malware behavioural detection is based around catching communication between malware and a command and control server. Either through sandboxed behaviour detection or by limiting the kinds of communication that is done with firewalls and intrusion detection systems. Some of this detection is based on rules but more recently pure AI driven models that auto generate rules and learn a networks behaviour have started to come on the market. 

## Current Malware writing methodologies 
Command and control servers are great at obscuring much of the code from a malware analyst, if they don't have access to all of the code then all they can do is analyse the code that is available. If it the malware was only alive in memory for a short period of time, this further complicates the issue of analysis [Diagram]. 

## Theorise holes in above systems/methodology 
## Present possible next-generation malware
There are a few ideas that I think would make interesting projects, truthfully combining all of them would be the most interesting but it would however be incredibly dangerous to create sophisticated malware as there is always a chance that it makes it into the wild. Therefore whatever solution I design should be an imperfect one. I also think that removing command and control servers from whatever solution I try would be prudent, as not only could they be compromised, but most security currently is geared towards detecting malware through it's communication with a command and control server. Whatever ideas I don't develop for the dissertation technical proof could still be mentioned as theoretical ideas that we might see in the wild in future; the ideas for a proof of concept are as follows:

1. Writing a piece of malware that is resistant to all forms of forensic analysis, even when a whole sample is given to an analyst.  
**Rationale:** As the malware would lack any command and control server, if it could truly be resistant then it would circumvent many of the active security processes outlined above. It would have to therefore also have no static parts that could be analysed, as this is the first thing a malware analyst looks for. So rather than making it entirely weponised, I could make a piece of code that is inherently symmetrical and has no obvious start and end point. If I also make a piece of code that also doesn't care what order the sections of code are executed then that would create a methodology for forensic resistance. For hints and tips to this possible solution I have looked into shapes of viruses and bacteria in the biological world and how virologists have problems there. There is also some fantastic work done into the math of symmetry thanks to origami and a branch of math by the same name. I also think that the only way to write malware like this in any significant way would be to do it using assembly language, although I will consult with thesis advisers before committing myself to learning assembly to that degree. 

2. Writing a piece of malware that can learn over time  
**Rationale:** Having malware that adopted current technologies such as AI would be an incredible feat of engineering. IBM released a proof of concept demonstration at DefCon a few years back with a virus that used facial recognition to trigger it, until it saw someone it recognised it lay dormant. It still used a command and control server to do a lot of the processes however, but it was a good start in incorporating AI into malware. I think the next logical step is to have genetic algorithms take a shot at learning how to run a piece of malware. For a genetic algorithm to actually show learning however, I would need to have them do something specific to make an effective proof. Therefore I think that either it should learn to reshuffle the entire code as part of the polymorphic engine, or it should look for multiple attack vectors and exploit them. The former seems much more doable than the latter in terms of time and code volume, even if it is likely it is the more complex of the tasks. 

3. Writing a worm that hunts for malware  
**Rationale:** Having malware that fights malware isn't a new idea, but it is fast becoming a particularly profitable one. In many data centres around the world they are using malware to sanitise the massive volumes of data that are just not feasible to get a person to do. Not only is it a matter of privacy for their customers not to have a person rummaging through their data, it's also a matter of time, as you would need thousands of specialised people to comb through that much data in a lifetime, let alone an ever changing landscape of users. With this example however, I would need to look at all of the ways in which we look for different types of malware and come up with an aggressive agent that would find them and at the very least isolate the offending data. For this methodology I would consider a command and control server to be acceptable, but any solution that involved one would be high overhead for a data centre and cost a lot of money, in part due to the fact that cost is measured in processes per second, and partly because it would create a lot of network traffic in a system that is supposed to reserve network traffic for legitimate business users. There are limited case studies that I've found so far however, as any worm made for a specific data centre would be proprietary technology. I can find some use cases and could look at algorithmic efficiency as part of the proof of concept however, making it a viable approach to a dissertation.

## Show proof of concept in full or in part
Although I cant possibly know how successful I will be at any endeavour before I've truly done the research, I can hypothesise how a proof of concept would look in each possible project however, and come up with an experiment and some initial suppositions of markers of success for each case. 

### Idea 1. Malware is resistant to forensics
Experiment: The only true test of forensic resistance is to have it forensically tested. I however can't afford to pay for such a thing so I will have to walk through the process as outlined in either Microsoft methodologies or through a book such as "reverse engineering for dummies" and see how much it resists. I would have to explain my methodology at each stage however to ensure that my previous knowledge of developing the malware didn't interfere with my forensic investigation. I might also write the paper in reverse order so that the breakdown of the malware is read first, to see if my methodology stands up to the sniff test before the reader finds out what I did with the code. 

Variables: For this experiment, I don't believe it would be necessary to implement any form of significant payload. Although the payload would be a big part of any malware, the bigger parts are; the polymorphic/metamorphic engines, communication/propagation code, and significantly the encryption/decryption engine. The malware could use simplified versions of all of these significant parts that are commonly already in antivirus databases, and I would use an old and isolated windows xp environment for a proof of working concept for the malware. In this way if the malware was to get out into the wild or something similar were to appear, we can then ensure that detection could be rather rudimentary following the logic in this paper, and that all the patterns of the code in this paper would be unlikely to fool current antivirus solutions as the ways in which it communicates and propagates would be highly detectable using modern firewall and intrusion detection solutions.

Markers of success: The major indicator of success will be that if I've followed everything in the guide book and followed a logical approach to reverse engineering the code, that less than 50% of the workings of the code and it's execution cycle can be attained. Another marker could be that symmetry is attained in the code without using techniques such as mov-fuscation, so that no static part of the malware exists, or at least no part of the decryption/encryption engine can be identified. Another indicator could be that using symmetry theory and observations of things in nature, could this work be the first step in that direction towards interesting worms that use code caving for non-concentric instruction execution.

Reflection: Did it resist reverse engineering in any significant way? Significant in this respect would be defined as at least 50% invisible/mislabelled disassembled functions, and/or broken instruction sets enough that no starting place or logical behavioural pattern can be determined. Exceptions to this would be easily observable system variables such as; length of time it takes to execute, shared libraries it accesses, amount of disk space the malware consumes. 

### Idea 2. Malware that is learning
Experiment: To test that a piece of malware is learning, I think for this experiment we will need to attack it in several layers. The malware must first be able to show that it is learning or at least adapting itself over time. To do this we will set up an environment of 5 machines that are isolated and can talk only to each other, using only a basic form of antivirus with no updates on 4 of the machines, we release a virus onto the 5th machine that then has the chance of infecting the other machines on the network. It should first create a copy of itself and send that off to the next machine and wait to hear if it is alive with a back ping. If it is alive then go dormant as a pattern that is undetected, if it is not alive then create a new shape of malware using different randomisation of initial variables and send this to the next machine, repeat until all patterns are exhausted and all machines are infected. Proving optimisation would be the next test, supposing it's infected all machines, what can it learn from analysing it's own dormant patterns? Is there a certain amount of padding that is working better, or a specific type of encryption/decryption? If I make it to this stage given the amount of time that I have then analysis in this regard could go on for years... might even be enough for a PhD. 

Variables: Controlling not only the state of each system and making sure that apart from the malware that no outside sources are writing to the systems will be the one of the biggest controlled variables. Also the antivirus that gets installed on these systems, although will have to be likely named and version stamped for peer review purposes, it should be stated that we are freezing it's effectiveness by not allowing it to update, and that a full test of all antivirus solutions would take too long to accomplish. But that if any antivirus was adequately stunted as we're proposing for the sake of this experiment, any vendors solution would do. The reason we will keep one machine completely unprotected is twofold; firstly we can record all of the information we need for analysis on that one machine so that we have data for our experiment, secondly it simulates attacks on either weak/outdated OS's on a company network or someone plugging in their own network device that is primed and ready to deliver such an attack. Both of which are not taken as seriously as they should be even after the NOT-Petya and WannaCry attacks. 

Markers of success: The first marker of success is for it to implement random seeds and catalogue the data, if it's something that can be programmed to be self-contained then even better. Then given this pattern data, can we use that to make suppositions about what patterns can be used next and what would make it more undetectable, or we could also send warning pings backwards containing flags for the configurations and locations of compromised machines so that each instance of the malware has all of the data of patterns killed and patterns alive to make decisions on it's next set of random data. As this list is not exhaustive, I think anything past this point would not only be a proof of concept, but also leave a lot of room for reflection and further work. 

Reflection: No doubt a worm that behaves in this manner will be loud on the network and also have a large code base, this should make it easy to detect if it was to get out in the wild which is beneficial for the ethics involved on a project like this. Because of the large code base as well, there is a good chance that it would become untenable as a for of malware code as it would likely; take too long to execute, not be completely storable in only memory, need a command and control server, and require a lot of code complexity which would make it easier to disassemble. 

### Idea 3. A worm can find malware
Experiment: To test whether a piece of malware can indeed be used to detect and remove other malware from a system, we first need to have a controlled and infected environment. I propose in stage 1 that 5 windows xp machines, 3 with the same malware on, have the worm look for the malware behaviour and delete it from the system. It should be programmed to detect abhorrent behaviour and not just look for the one specific malware that is on the machines. 2nd stage we should infect 3 machines with different types of malware from not only each other, but also from the original malware in stage 1 of the testing so that proof of the codes ability to detect abhorrent behaviour can be measured.  

Variables: It may be prudent to use only one type of malware for detection such as a trojan, just so that the types of behaviour that we are detecting is limited to a smaller range than if we were to make a "cure all" worm that could detect anything. That way, given my limited time, there really is a chance that something could be developed to detect any kind of trojan like behaviour for instance. 

Markers of success: If the worm can be programmed to propagate through the network and detect 50% of the trojans, then it could be considered an avenue worth exploring for further research, and would serve as a proof of concept for a dissertation I feel. 

Reflection: Look at different ideas about how the code could be optimised, how it could look at more behaviour and how it could detect more types of malware. I could also look at algorithmic efficiency and if less clock cycles or memory could be used for the same amount of detection, as every data centre that might run this code will measure cost on use of resources. 

### Evaluate my effort and other possible avenues
Not only should I critically evaluate my own efforts, I should also reflect on if my efforts are the only security circumvention likely to be out there given current technology. Avoid Quantum computing like the plague however, partly cause your marker hates quantum, and partly cause there is little evidence that quantum anything is any use in a malware type solution. Not only that but quantum solutions are impossible to reenact in classical architecture with any real efficacy and therefore the point is moot for a spreading malware in mainstream computer architecture. 

## ADVISER HELP PLEASE!!
- [ ] [help please](#title) title remains a problem. We should spitball ideas 
- [ ] [help please](#present-possible-next-generation-malware) could do with help narrowing down which one to technically implement. 
- [ ] [help please](#ethics-considerations) We should find time to talk about ethical considerations as I've never written one before I'm not sure everything that should be covered in one.

## Advisers feedback/ideas section
As I have multiple people looking at this form, please use this format for any paragraph you note here. For each paragraph, please also make it a concise idea or train of thought for one point per paragraph, because although you're more than welcome to have multiple paragraphs, it helps me keep track of each idea more readily. Think about it like reditt but in a single document. The format then is...

- [ ] [Your Name](topic section link) Point you are making about the given topic and two trailing spaces or one empty line separating your paragraph from others. This is so that it formats nicely in the preview, and the tick box is for me so that I know that I've read it. 

Happy commenting on the run!!

## Ideas space
IMPORTANT! This space is for my ideas ONLY! Advisers wanting to comment on them please use your section above.

Could string bit sections together to make randomised patterns. The problem starts at the initialised bit section, if it is the same each time it is as good as having a static encryption engine. Instead, each section should be encrypted and agnostic so that any bit pattern could be used to start. We could do this with jmp instructions that are randomised by integers... a proof could be written in python, but it might be better in x86. 

How to avoid behavioural recognition??

Python is really good for self modifying code as I could use `eval()` or...
[library](https://github.com/julbov/reloading)

https://stackoverflow.com/questions/1830727/how-to-load-compiled-python-modules-from-memory
    
path poisoning...   
chi squared test [books](https://www.greenteapress.com)  