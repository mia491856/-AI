def makeURL(**kargs):
    myUrl="http://123.154.163/index.php?"
    for k,v in kargs.items():
        myUrl += k +'=' + v + '&'

    myUrl = myUrl.rstrip('&')
    print(myUrl)

makeURL(user='psychoria', index='5', page='10')
