def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    n = len(rater1)
    label1 = {}
    label2 = {}

    p0 = 0
    for i in range(n):
        if rater1[i]==rater2[i]:
            p0+=1
        
        if rater1[i] in label1:
            label1[rater1[i]]+=1
        else:
            label1[rater1[i]]=1
        
        if rater2[i] in label2:
            label2[rater2[i]]+=1
        else:
            label2[rater2[i]]=1
        
    p0 = p0/n

    pe = 0
    for label, val in label1.items():
        if label in label2:
            pe += val*label2[label]
    pe = pe/(n*n)
    
    if pe == 1:
        return 1
    else:
        kappa = (p0-pe)/(1-pe)
        # print(p0, pe, kappa)
        return kappa
