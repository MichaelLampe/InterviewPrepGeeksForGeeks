from timeit import Timer


def maxProduct(words):
	"""
	:type words: List[str]
	:rtype: int
	"""
	words.sort(key=len, reverse=True)
	sw = [set(x) for x in words]
	max_val = 0

	front_pointer = 1
	back_pointer = 1
	local_max = 0
	while back_pointer < len(words):
		val2 = sw[back_pointer]
		l2 = len(sw[back_pointer])
		for x in xrange(0, front_pointer):
			if len(val2 | sw[x]) == l2 + len(sw[x]):
				val = len(words[x]) * len(words[back_pointer])
				if val > local_max:
					local_max = val
		if local_max > 0 and len(words[0]) * len(words[back_pointer]) < local_max:
			return local_max

		back_pointer += 1
		front_pointer += 1
	return local_max

array = ["nehgeh", "chmdimj", "ngimmdeaafhonbilncooeadk", "cngcedpcnnhjmbffmelo",
         "kjihomgmocecofncmideokmelhhfhbndepeh", "amgmlpoiblofppedkmfooam",
         "olikoonefcmlopeoabifbldcehnbbaejnloedaeoo", "mfffkghenhclffmlahkglengmnabgnacjpijija",
         "ifkbdjbhhjibcdmkhfhmochbhjgcphbagldjeocbkk", "eebinafpfojdjfbppbejhoagl",
         "njogfhkoceohhnbbbdiccocokpbgbofjflimchifei", "jopjmamlfnblbapgmlhlfokhofeocdbldj",
         "pcpckfeegoiakpmghlllcghglfboabpkpgdkdmcfebcgpmklijn", "biigobjpopd",
         "fjlinbffbfjeehbonopjachddfpfgkoifokedflh", "oonilkeombbobicmgjfpdfddnnbmpccn", "gklhcmaacmjimmehm",
         "cekllmagpjlpjkkfjpip", "oeeocnhoanekeibdekkpgkkkkhknbkkpfbcdhgmicheghjfafm", "dacelplloaefjhlaohbhogjfec",
         "kkkdoippmdkmmjpmolljjbn", "aiaalfdgdnpadncijjofobdnhoffedhclmgaemkdkhdgalekm",
         "ghhjmgepmcjncgccpnbphmmaobihjpmcecglknjagghgkha", "lhmlflolbefmockcag", "kkoabkj", "eaf", "eclcebi",
         "amidgcjimaecempih", "knlmljnpcminghbmlipijagnk", "mejpdlmkmiabjnchjblfhgbgbc",
         "lohgffenhjhbnjnnocfhdgnckllcfdlhfpcjggmnalleake", "lali", "lbkoegkagabelohplkhcmndicjaie",
         "oimmmigkkngcfncdknhkfombmonapmbfbagoddalfgifhmecha", "ieepbdpe", "gngdgflnefajg",
         "hdnhpcclihlphkebnjdfjpkkakenelcoaipblaafofnnjngp", "bgnnhkhamnl", "lamhjlfoegl", "ockmfnpnkigi",
         "oikonddmjemlnfkgdmiinbakal", "enfeffmbgggcjmoafmcbabipmfldehcgfmljnknabmookioo",
         "coflkefndndhfdpkanpfmoibccaofo", "epbp", "ppjgoacdeglgmapb", "cgchcfdiecajapodfehgecoojkkfmkikofj",
         "aobdk", "nomhainlfojcbngaihcoicaomblonepcclin", "gbhfcdgpaladipmbahdclfleieknkmdfgjhbfko",
         "ncgkopnmginchkdffohlciamdn", "kddochdjoaiejlefnnonninofnklpfkejjckfakhcabejmfimg",
         "clbdeafmohmlmhkfngnijiohefnhobbgblndim", "jigfinceipcghpigmn",
         "locpmnodnhafdbghdnkcbofpegmgefcoifhjbnddp", "anmjopaoeholhniomncmakllcacfiagafmhopp",
         "hloihhljjklbiadcnccpogajkokogapaogcnafjbemf", "ieej", "ibinnh", "ejpm", "jlakjcoimgihkhobbikeehhgcjh",
         "efljkffnkfnbgoaenaoddimolpjldhfbpajcnk", "jphijfkbkkmcjjkkjebahiilcekboa", "nbkjmbpdhbcaflmlclegphn",
         "gfkgkkmhffdehhdimponghaaogkndhejoncajjpje", "mppbnfgbchmffbnkjkkbdjfmfo",
         "lecbddlppngbjakgidoomiijilhoednmhemfaa", "ncddphlhdogejgnpadcicbbakegldcc",
         "ginjcggdhjaffppefbebfaemkoienofgbifdjeak", "babaaajnecobdejpbgdijdhjkfpojjpaidkkibe", "npf",
         "ggkjpkhlbmanlcfbnhbpenddjnaheefgajkniifo", "laonlogoeiokgolkojkpgmhkhgocgojagnfgancdga",
         "pepadmjlgfhddcjdofhnabpchmjedgfal", "pdjpbmfkfiekeibikplc", "eeeclpipefdfncpneokhleggmlf", "ohodeha",
         "hkaeehfeijkmceadhbjebljnkekkgoemcddmlgebf", "gmbjnapoafpilieiafjgdaeikklmfojadjbhbneobbafiofa",
         "gdgdmfnfilkcfnidmkgjlo", "hmakapglgkbpphkpfcaijejinahbcpamnlchecgfbpobbgago",
         "enkfkgphgnjpdfnhekaipfhddgcdmfckpkhnamncmdnjpkn", "egmfdefjnpnnhcllgfcgnlonleibjdgg",
         "hmpdnkljfohlhefjcmkbaicmfpcnahdhgnkfcedl", "mdepdlfcecockooeapbcacbcjggjcneoefihnddaa",
         "phnnphifblgclpmobcjfkhcflpmjonpc", "ngbimpfbnladanbjdnlpcblieelahcdahifjcfifhc", "cfonlodda",
         "fjchdenejhajbioenbngomfijjiealnjpknh", "mfepojofdnndbabijagipbhdamnkjegdjmkfleoj",
         "dgiadmhemoknogcfgohdapelaonkfg", "ailfhodmcfjbhgelmngbikmhodpcgieohckdkimipfkopbghmh",
         "leffmneagfnohjdfomgiekjfhfmmjac", "ncchobmmhgfckokjohpnmnjmkaiogaloielbjdeakfgiloopnk",
         "kiliiknmlpbdbdmbfpdmigjil", "nclhdomnfohjppadbegnglfdfmigcalhehnc", "maaikfldbfchpmolefgkahgoddbejioji",
         "gajcjoihfhgkiglongoa", "iocdlopacncofjdmif", "ndieekcdcbocnkfcieelleapjmmieaglfpbploj",
         "cnhmfnmpmedpkmbohcmgkaadhe", "pboafkhionnhdmgjllmldabcbeoigkmpajkfoioffanmpkc", "poeakopgeff", "boek",
         "jafiahgpmegdpcdicffpilpmpof", "ficmjhefngcmiejaahcijpm", "mjoblfhifopkghehbncahalacipjioalgi",
         "nmighpcdaibblecaimi", "empolligfogpfcbfehpglbaodbfkfpdpfacc", "lmbmclncdijlc", "ajb", "hpcfc",
         "lboppcngfjiahan", "hooimjminnabnjdmibfcpghbacempndfhfbbnchjplc",
         "ibjnedcjcifenhdgkgklnmlghalchcmigjcomanopmaal", "flpnibakdael", "bjceeigibjokmkfhbnbohkmfnidcoakp",
         "gcdihejbehdfiknloojleimdapjko", "aphmhjdeojamaabcnjmhafghicccjekkpebccakpiobbg",
         "afaidgnmipdjbamnkccpmejiofifgnbkfdkeecebmeknoofni", "llaggnenahlhgemcckglmanlkaeldkknengdejagkgh", "gdji",
         "gdpkdomkjgoceilfjekdlcpn", "iibefnkninhlggdghdk", "mnddgbefbci",
         "dckakkdjiagnohiiidjabnpklpmfbpfkpodbagmmockhcjcd", "ook", "eagandhclhdejhakdfgcbkkibfgghelhg",
         "iljedokcjgpelfannpceebpkaag", "nmogciglmenlpobjljgmenaimjjjhobkcofadimm", "ienbofldeccchneg",
         "jmkldnidkngkbkiiicfagckonciljhbbnhhgmkikhmcglabilff",
         "jddgbnpcmecekgbdjdpfkikdckfkaopgaaagkbnajoiabmdicpl", "ohekamloakogijldijneccmmbjelbbnkkcmiaopnddc",
         "cadalfpjooobhllejeoclcmohnmjdomaaiaamnokfbekphfcb", "mlbmdpeahojgpabgcmgpjfeipahfghichlojffgcndflfgnpjak",
         "fbdlgikhnpghkdllcnejjhemh", "oogicmggpaikcnkhnhcag", "jnddmbmllpcecbajeilm", "dgeoklakadkefl",
         "gjlmaiehammahnkenpffookafohkapimlekgholekkmfjaag", "cgehmigocioinmohkbegoinaomdcippkiapdp",
         "hncifhjmkobongmbjlfelelpkepkpefmjapif", "icnichgdcdplbkikaoelpboojeeko", "dpedaelbhnmplknaebpocdnhcg",
         "nkingocanpffleodinoibcffjkh", "hpchlfdgffhkliifmejj", "gpbnmcncakbcknijkgofa", "kenekdjgieih",
         "nabcdobocghijeipcffpg", "gpalcdggnokdapmfgpiaiaeahalomkpmohdejnpjdpojaa"]
array2 = ["ccd", "accaceddeeeaefc", "bcaffa", "bbcfafbb", "accacfebbabbeedfbfdb", "beddecbffcdaededdaefdedfdea",
          "cf", "ddafdcbd", "bbafacebacaefdaffccebddff", "ebccffcddbeddccacceccaec", "becfbfdccdfdeadfbfaddbcded",
          "cbabeaaeabefedbaeaedc", "dfadbbdbead", "cafaefdcd", "eccdbfceafeeeacfcddc", "dbabbcdbb",
          "abfbfbffcbebde", "cfaadaa", "fc", "faebcabb", "adbacebabcaaccbdeaffff", "aeaefccf",
          "dbacbeeabdbcdfccabebaecfef", "ecdadeefcaddffaececffa", "defcabf", "abbcecbccbdaebaecaefabed",
          "dfeeebcbaaefc", "aecccbcbbdddb", "dcfabacec", "fccfbacbacddeaaea", "dfdbfacbacbecb", "cbfeebdbfecb",
          "cffaacacbde", "aafd", "bdcebbbebd", "afeffadcfcdacfba", "dafeefbcdfaffcfacee", "dcbbebfbedafedcdbab",
          "cafaf", "bcbcccfdebdd", "efaaaacccff", "cffbead", "ebcfccfcddffdec", "fffdfdcec", "beeafefbdfa",
          "cdfdbccfbaaeffcabab", "ddadcbabbcb", "decfaeabbecebaebeaddedae", "cdcbfffbebae", "aeccefcbcbbddfdc",
          "ffefedaf", "cddbabccafaffeafeedcbedbdad", "eddeeccfedcefadfdfebfacb", "aca", "ffdcafaddcddf", "ef",
          "bbbbffe", "ffccfebabaadcffacbbb", "cbdeddfddffacbeeeebafebabda", "ddeecb", "cffdc", "edcffcebadf",
          "becbcadcafddcfbbeeddbfffcab", "abcbaceeaeaddd", "cfeffceebfaeefadaaccfa", "eaccddb", "caeafbfafecd",
          "becaafdbaadbfecfdfde", "ecabaaeafbfbcbadaac", "bdcdffcfaeebeedfdfddfaf", "dbbfbaeecbfcdebad",
          "cceecddeeecdbde", "beec", "adbcfdbfdbccdcffffbcffbec", "bbbbfe", "cdaedaeaad", "dadbfeafadd",
          "fcacaaebcedfbfbcddfc", "ceecfedceac", "dada", "ccfdaeffbcfcc", "eadddbbbdfa", "beb",
          "fcaaedadabbbeacabefdabe", "dfcddeeffbeec", "defbdbeffebfceaedffbfee", "cffadadfbaebfdbadebc",
          "fbbadfccbeffbdeabecc", "bdabbffeefeccb", "bdeeddc", "afcbacdeefbcecff", "cfeaebbbadacbced",
          "edfddfedbcfecfedb", "faed", "cbcdccfcbdebabc", "efb", "dbddadfcddbd", "fbaefdfebeeacbdfbdcdddcbefc",
          "cbbfaccdbffde", "adbcabaffebdffad"]
array3 = ["dgahmncghaolfdonnbefpmfkidnpiaoancmdjgbebdajbbdjj", "ljjkdohpobkdgd",
          "gfnobekjeaagnbipphopnggbbchjlaokhmfjcclia", "ppebcdoofgfodeakgmnpcgf", "nlcjm",
          "cfgellnpbcoldeleoominjcblhfddphaf", "landbohhgmbplcgdpdgjdkinbmh",
          "ljgpjiooejjlhnleegjdjkobjbdamdcaipddpbpoedb", "dbangblpgiigkeghhijbmgfgefidhgdeebdeglfn",
          "loomphijnlhfjdnlegpdpinnfk", "lamniilf", "egjelephjbnighjegbcn", "lfkjbiah",
          "egpkjopglgocfeiocfmfknebhcppjjlgaecpnf", "aklpinlb", "jhdhg",
          "khlcgapeghpkgjppajdnbpbfgoeoidpmagmpgbkdhikclgb", "mjnilicgnodlndffhmjjgjkkmbenpdohdjplpboacc",
          "jcaekpbamkbifmdc", "jbafdoafhbbmdddimem", "cajobhpemfkfconpbhfflkahciofnoenop", "odakfaplbmncngdgfnpk",
          "blkmofhbhffpiflebjblppfmhkckehpdd", "eecjnndbimdmjk", "ijdkijhdichbngnn", "kbdnnnhegiddbhle",
          "fcdjmcmhgbnbgkbmpa", "hejgdijfcfijbfaglfgbmobkdhlgjpiemoal", "mbfcdknko",
          "ijoiegobpikdcemakmhpanmmkbcejjkjmmngjcle", "hphhcmel", "iookikkhilemfelcg",
          "kajhalmhcdnnhdffcdbgabmiidciljpfnepgkibj", "bakhgjbfndhmfegloaeellkflh",
          "eoddgjnjieifdopmijenehmhlldnjmpmedcaeo", "fallaoenaalbdcnfjcligkopmpiohjffbcngnappmn",
          "lmbgbhkalcobennoobkmfaifbiflcjbmocmabpnnbddhc", "dnnipbgbihbikfamdkfh",
          "gpinplmdlcigjcmncjganklcjghejdgpijcldfmecnnplob", "dpafhpfobchoojiaeofimbjdhmhjdlpnppefojbpcmioefhe",
          "pjhnbagmflfeoamhfjkmnlj", "hnhnnacglomgeiilapfgphjlhfdkae", "mlpppdebcfhohoiolfnlojbe",
          "obofbpnpajlglcabpnaofoepikbfcjcdmfcnngmibb", "gonmghpgg", "gkhkjbpgakaahim", "flcipjbijilomkajincjmap",
          "hicejflafdcknahbmakbnimpamibadccogajfdoednhmcn", "bjap", "bpcmpbicjnegkbhjmbnanekpbljpjheicefeogjhmj",
          "lhijpceccbljmoopinlpliiiiikandfaaioaakpgh", "kfbibggkjmkdgmkhnmo", "gimejmhaehlgojhgdembnajifemh",
          "elamkahmcjid", "cadlfgojcplpcampojijkgjbdjbfifkfljklkgabkljmgkkgae", "dilagdpdeph",
          "oboenhpnfklgflhhcpamfi", "hpdledlbebikledjmlpgco", "abgakcedjdmipknpfk",
          "bdpmgnlkledjpiiggbflfifkdiocinifmp", "meafpekmljjeigpgckhjpmladddepibcmhpfbijejepigjok",
          "pnipkekjlkocol", "gdefiemgpbmbagmkaggicnjkfm", "dapaapjedlejkfpkahahbcfhipcmbaolcikjpoafibpkdic",
          "hnipakdobdkgcehjhgkblnm", "nfipifkcflhfcakfjhpjpapjbgbbhccakolmnhfi", "klkaodieiejmndffdmogm",
          "mapfcohailkdgjfahebljjfgfahdonndlhdpdhnokainofhnedd", "dpakhehhbcplaiio", "hhlchlkkdeiahjpodhgdkj",
          "ecgbpccnmcojgjldabajlagpkdfmaehdfo", "beblfekckekklpf", "odl", "poiaehk",
          "hplbknjjpdabcaidjnpghaddbpbdhhcojojckniibfpob", "odgdagdijihfbbgimcagplobcpbilhpdkfcgdabldame",
          "bilideb", "pidbfmekblgieicc", "dfgblekonahibahbipbgagpmhmceabdmokiii",
          "ijehmedllccppleahcddiplicfeobbfinlbneellgp", "pgnmhpajcpanfopjnebgldhmcdiooilmmliejahneieheh",
          "jpkogaopbhngimohmohnipcpap", "fjilikmagklfmhohkdlc", "ahkcjkmkgcgkadofdkhk", "penfhpgfbbfiebe",
          "jciiakhlcplmkbinppjpgjkimhigmamalpifmfaojji", "eanhfimiipncfakabbkllnhnkmcme",
          "khckkeclkfklbiinljlacnfekgncdn", "obnamapoieccfchjamifppnkdgnddfkcdhaehcemihdlgcoop", "godj",
          "ipinlpecnijkalkdcnhlhlldegkbicpkelbmhc", "mblgpnihcillkhcmai", "amk", "edifopfldfjfdpjfooheajhlanb",
          "dfjpeoajmmpfdakjiadil", "lehnmddmlfmahhjgodhmikb", "koampmhgbce", "pjkekkoip",
          "denmpkdgedadggnldclhefehjopfeellnbknlkhccajiffmk", "oi", "mcilgf",
          "anebeggmjjcmabmokbchpibdhbeknoemfnglocipanbk", "hnfkdfhakbnmlpcipdalpikaolggnn",
          "bkhomfbmdfbeklbphalkebmphackgfghjilndjafflbncdi", "knfbmhiaeklnj", "bfdfmecdihnckljpgjpioc",
          "naiiededhaaldmpibadmml", "opfmaegjkfgnmbhmnckbcfoognienndmnocmnnigdlopmdo", "pcadefhfa",
          "aadmlccdfpahmin", "kjd", "cniolkpincceggghmekjji", "lnabempbemhjcknalojbdofm", "kidpibngoage",
          "cgifhjlegcgomiphgphfkagkboodnmgmbp", "gkpcededddnfcandfcadllmfgcipkofbpfg", "kmbppbkbnmcbg", "ola",
          "kacciockojplfljoolgahhcfdfnf", "mfonckjmhpga", "ooaleeljoalhphoamfokmhnpgfdp",
          "blelncpbljafdbhiglbofiepcafm", "kkacnbki", "aoffmfjofjpjgjmoohnipkhm", "fgpjoefijb", "pcnmpk",
          "kbhiebinephfkpcnaigfiphdbeamaapfdkkeefplhine", "jjmijncicghnigehigoccogdmdk", "pioiipkigblimeabhkj",
          "nhmdemacgpeegggdahlkhgckfebgddnfihcnlmilpimdmeocog", "ogbooeeceblmhhoaacaplmlaaheoagbepgdbpnpcf",
          "opanicpmj", "cdcgecidpdllnd", "pfkecfnebkkbmhnacfljnojjobhihnkagpc", "naajiapnlikel", "nblnpgjicnigic",
          "pnhpnnbicffencbmhagldnpifnnneifkmikaojicnkbgkjcm", "mjmkpalblfpoidgdakbkledlikdiephonlo",
          "poemgbaibemnpeaedmgadjljbpkibpabmjiafkobdcnpfbnlfc", "cmlackefgdkkcoiffiedjjidl", "hgnpgfcle"]

def test():
	maxProduct(array)


def max_product_forums(words):
	"""
	:type words: List[str]
	:rtype: int
	"""
	maskLen = {reduce(lambda x, y: x | y, [1 << (ord(c) - 97) for c in word], 0): len(word)
	           for word in sorted(words, key=lambda x: len(x))}.items()
	return max([x[1] * y[1] for i, x in enumerate(maskLen) for y in maskLen[:i] if not (x[0] & y[0])] or [0])


def test2():
	max_product_forums(array)

def max_prod(words):
	words.sort(key=len)

	# Possible characters is the key
	# Length is the value
	v = {reduce(lambda x, y: x | y, [1 << ord(c) - ord('a') for c in word], 0) : len(word) for word in words
	     }.items()

	max_val = 0
	for index, val1 in enumerate(v):
		for val2 in v[:index]:
			if not (val1[0] & val2[0]):
				if val1[1] * val2[1] > max_val:
					max_val = val1[1] * val2[1]

	return max_val

def test3():
	max_prod(array)

# Union = 1.08
print Timer(test).timeit(100)
print Timer(test2).timeit(100)
print Timer(test3).timeit(100)