tweet1 = u'@twitter meets @seepicturely at #tcdisrupt cc.@boscomonkey @episod http://t.co/6J2EgYM'
tweet2 = u'\u9023\u62953  RT @IWJ_ch4: \u83c5\u300c\u5e02\u6c11\u6d3b\u52d5\u6642\u4ee3\u306e\u4ef2\u9593\u306b\u306f\u53cd\u539f\u767a\u3082\u3044\u305f\u3002\u79c1\u3082\u3067\u304d\u308b\u3060\u3051\u539f\u5b50\u529b\u30a8\u30cd\u30eb\u30ae\u30fc\u306f\u904e\u6e21\u7684\u3068\u3044\u3046\u4f4d\u7f6e\u4ed8\u3051\u3067\u3001\u6bb5\u968e\u7684\u306b\u8131\u3092\u4e3b\u5f35\u3057\u3066\u3044\u305f\u3002\u305d\u306e\u5f8c\u3001\u5b89\u5168\u6027\u306e\u78ba\u8a8d\u3068\u3044\u3046\u524d\u63d0\u306e\u4e2d\u3067\u306e\u6d3b\u7528\u306f\u3042\u3063\u3066\u3044\u3044\u3068\u8a31\u5bb9\u306e\u65b9\u306b\u5909\u308f\u3063\u305f\u30023.11\u3092\u7d4c\u3066\u3001\u6b63\u3057\u3044\u3053\u3068\u3067\u306f\u306a\u304b\u3063\u305f\u3068\u601d\u3046\u300d'

print 'Tweet1:',tweet1
print 'Tweet2:',tweet2
print
print 'Number of characters in Tweet1:',len(tweet1)
print 'Number of characters in Tweet2:',len(tweet2)
print
print 'Number of bytes in Tweet1:',len(bytearray(tweet1,encoding='utf-8'))
print 'Number of bytes in Tweet2:',len(bytearray(tweet2,encoding='utf-8'))