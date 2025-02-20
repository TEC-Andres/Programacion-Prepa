"""
#       Sesión 10: Assignment-08
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: nptolatex.py
#
#       Creado:                   20/02/2024
#       Última Modificación:      20/02/2024
"""
import sympy as sp

def expression_to_latex(expr_str):
    # Define the symbol x
    x = sp.Symbol('x')

    # Parse the expression into a sympy object
    expr = sp.sympify(expr_str, evaluate=False)

    # Convert the expression to LaTeX
    return sp.latex(expr)

# Input expression
expr_str = """
- 7883724611579467 * x**48 / 6546781215792283740026379393655198304433284092086129578966582736192267592809349109766540184651808314301773368255120142018434513091770786106657055178752+ 59030303209229 * x**47 / 12486994201263968925526388919172665222994392570659884603436627838501486955279062480481224412253967884639307724485626491581791902717153141225160704- 5409705322334541 * x**46 / 1560874275157996115690798614896583152874299071332485575429578479812685869409882810060153051531745985579913465560703311447723987839644142653145088- 7251173601194131 * x**45 / 1524291284333980581729295522359944485228807686848130444755447734192076044345588681699368214386470689042884243711624327585667956874652483059712+ 5554983705471745 * x**44 / 5954262829429611647380060634218533145425030026750509549825967711687797048224955787888157087447151129073766576998532529631515456541611261952+ 4512161624614713 * x**43 / 726838724295606890549323807888004534353641360687318060281490199180639288113397923326191050713763565560762521606266177933534601628614656+ 7792824007571373 * x**42 / 1419606883389857208104148062281258856159455782592418086487285545274686109596480318996466895925319463985864300012238628776434768805888- 5571385768479291 * x**41 / 5545339388241629719156828368286167406872874150751633150340959161229242615611251246079948812208279156194782421922807143657948315648- 5510354483620003 * x**40 / 676921312041214565326761275425557544784286395355423968547480366360991530225982818124993751490268451683933401113623918903558144- 3242325404383229 * x**39 / 330527984395124299475957654016385519914202341482140609642324397637202895618155672912594605219857642423795606012511679152128- 8836003893408847 * x**38 / 2582249878086908589655919172003011874329705792829223512830659356540647622016841194629645353280137831435903171972747493376+ 1227128513428787 * x**37 / 157608024785577916849116160400574455220318957081861786671793173616982887085988842445657065019539662563226511961227264+ 4944163194387397 * x**36 / 307828173409331868845930000782371982852185463050511302093346042220669701339821957901673955116288403443801781174272+ 8339369137070963 * x**35 / 601226901190101306339707032778070279008174732520529886901066488712245510429339761526706943586500787976175353856- 1886028389254045 * x**34 / 4697085165547666455778961193578674054751365097816639741414581943064418050229216886927397996769537406063869952- 172641468729141 * x**33 / 8958978968711216842229769122273777112486581988938598139599956403855167484720643781523509973086428463104- 4058794052354197 * x**32 / 139984046386112763159840142535527767382602843577165595931249318810236991948760059086304843329475444736- 4910559606413859 * x**31 / 273406340597876490546562778389702670669146178861651554553221325801244124899921990402939147127881728+ 6680543723959995 * x**30 / 533996758980227520598755426542388028650676130589163192486760401955554931445160137505740521734144+ 2845275490350237 * x**29 / 65185151242703554760590262029100101153646988597309960020356494379340201592426774597868716032+ 6061079622203343 * x**28 / 127314748520905380391777855525586135065716774604121015664758778084648831235208544136462336+ 8804608559281781 * x**27 / 994646472819573284310764496293641680200912301594695434880927953786318994025066751066112- 6565044971059765 * x**26 / 121416805764108066932466369176469931665150427440758720078238275608681517825325531136- 2617408822067911 * x**25 / 29642774844752946028434172162224104410437116074403984394101141506025761187823616- 1258943564575999 * x**24 / 28948022309329048855892746252171976963317496166410141009864396001978282409984+ 487148419302815 * x**23 / 7067388259113537318333190002971674063309935587502475832486424805170479104+ 4108287090259459 * x**22 / 27606985387162255149739023449108101809804435888681546220650096895197184+ 8295503302919685 * x**21 / 107839786668602559178668060348078522694548577690162289924414440996864- 3449069861818673 * x**20 / 26328072917139296674479506920917608079723773850137277813577744384- 3147602163593051 * x**19 / 12855504354071922204335696738729300820177623950262342682411008- 2770940926241257 * x**18 / 100433627766186892221372630771322662657637687111424552206336+ 2092075823767077 * x**17 / 6129982163463555433433388108601236734474956488734408704+ 1494426653825771 * x**16 / 5986310706507378352962293074805895248510699696029696- 2387172891684749 * x**15 / 5846006549323611672814739330865132078623730171904- 5218316418399643 * x**14 / 11417981541647679048466287755595961091061972992+ 7442597091811145 * x**13 / 11150372599265311570767859136324180752990208+ 1123370411054593 * x**12 / 2722258935367507707706996859454145691648- 937736816752119 * x**11 / 664613997892457936451903530140172288+ 3628615908090653 * x**10 / 2596148429267413814265248164610048- 128019377258789 * x**9 / 158456325028528675187087900672+ 1529957831312645 * x**8 / 4951760157141521099596496896- 6276919242962477 * x**7 / 77371252455336267181195264+ 1106436975094145 * x**6 / 75557863725914323419136- 4190783080742605 * x**5 / 2361183241434822606848+ 1268972169941043 * x**4 / 9223372036854775808- 1820646636526713 * x**3 / 288230376151711744+ 369569744279505 * x**2 / 2251799813685248- 8858482322086445 * x / 2251799813685248- 6429084652883401 / 2251799813685248"""

# Convert to LaTeX
latex_expr = expression_to_latex(expr_str)
print(latex_expr)
