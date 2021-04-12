def WordCounter(OurString):

    Counts = dict()
    Words = OurString.split()

    for word in Words:
        if word in Counts:
            Counts[word] += 1
        else:
            Counts[word] = 1

    return Counts

TheString = "Talks between Iran and the USA to revive the 2015 Iran nuclear deal are set to resume. At this early stage, the discussions will be indirect and there will be no face-to-face meetings between high-level officials. The discussions will take place in Vienna and European officials will act as intermediaries. On the table is the revival of the 2015 pact under which economic sanctions on Iran were eased in return for curbs on Iran's nuclear program. This pact was intended to make it harder for Iran to develop nuclear weapons and was abandoned by Donald Trump under his administration. Officials in Tehran have always denied they have had any intentions to develop such weapons."
print(WordCounter(TheString.lower()))
