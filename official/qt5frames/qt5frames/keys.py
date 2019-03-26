# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

from asyncframes import Event, any_, _THREAD_LOCALS

class Key(Event):
    def __init__(self, name):
        super().__init__(name + " key")
        self.name = name
        self.isdown = False

class AnyKey(any_):
    def __init__(self, awaitables):
        super().__init__(*awaitables)
        self.__name__ = "any key"
        self.name = "anykey"
        self.singleshot = False

    def _step(self, sender, msg):
        sender._listeners.add(self) # Immediately re-add self as a listener to the pressed key
        super()._step(sender, msg)

class Keys(object):
    def __init__(self):
        self.escape = Key('escape')
        self.tab = Key('tab')
        self.backtab = Key('backtab')
        self.backspace = Key('backspace')
        self.enter = Key('enter')
        self.numpad_enter = Key('numpad_enter') # Typically located on the keypad.
        self.insert = Key('insert')
        self.delete = Key('delete')
        self.pause = Key('pause') # The Pause/Break key (Note: Not anything to do with pausing media)
        self.print_screen = Key('print_screen')
        self.sysReq = Key('sysReq')
        self.clear = Key('clear')
        self.home = Key('home')
        self.end = Key('end')
        self.left = Key('left')
        self.up = Key('up')
        self.right = Key('right')
        self.down = Key('down')
        self.pageUp = Key('pageUp')
        self.pageDown = Key('pageDown')
        self.shift = Key('shift')
        self.control = Key('control') # On Mac OS X, this corresponds to the Command keys.
        self.meta = Key('meta') # On Mac OS X, this corresponds to the Control keys. On Windows keyboards, this key is mapped to the Windows key.
        self.alt = Key('alt')
        self.altGr = Key('altGr') # On Windows, when the KeyDown event for this key is sent, the Ctrl+Alt modifiers are also set.
        self.capsLock = Key('capsLock')
        self.numLock = Key('numLock')
        self.scrollLock = Key('scrollLock')
        self.f1 = Key('f1')
        self.f2 = Key('f2')
        self.f3 = Key('f3')
        self.f4 = Key('f4')
        self.f5 = Key('f5')
        self.f6 = Key('f6')
        self.f7 = Key('f7')
        self.f8 = Key('f8')
        self.f9 = Key('f9')
        self.f10 = Key('f10')
        self.f11 = Key('f11')
        self.f12 = Key('f12')
        self.f13 = Key('f13')
        self.f14 = Key('f14')
        self.f15 = Key('f15')
        self.f16 = Key('f16')
        self.f17 = Key('f17')
        self.f18 = Key('f18')
        self.f19 = Key('f19')
        self.f20 = Key('f20')
        self.f21 = Key('f21')
        self.f22 = Key('f22')
        self.f23 = Key('f23')
        self.f24 = Key('f24')
        self.f25 = Key('f25')
        self.f26 = Key('f26')
        self.f27 = Key('f27')
        self.f28 = Key('f28')
        self.f29 = Key('f29')
        self.f30 = Key('f30')
        self.f31 = Key('f31')
        self.f32 = Key('f32')
        self.f33 = Key('f33')
        self.f34 = Key('f34')
        self.f35 = Key('f35')
        self.super_L = Key('super_L')
        self.super_R = Key('super_R')
        self.menu = Key('menu')
        self.hyper_L = Key('hyper_L')
        self.hyper_R = Key('hyper_R')
        self.help = Key('help')
        self.direction_L = Key('direction_L')
        self.direction_R = Key('direction_R')
        self.space = Key('space')
        self.exclam = Key('exclam')
        self.quoteDbl = Key('quoteDbl')
        self.numberSign = Key('numberSign')
        self.dollar = Key('dollar')
        self.percent = Key('percent')
        self.ampersand = Key('ampersand')
        self.apostrophe = Key('apostrophe')
        self.parenLeft = Key('parenLeft')
        self.parenRight = Key('parenRight')
        self.asterisk = Key('asterisk')
        self.plus = Key('plus')
        self.comma = Key('comma')
        self.minus = Key('minus')
        self.period = Key('period')
        self.slash = Key('slash')
        self.zero = Key('zero')
        self.one = Key('one')
        self.two = Key('two')
        self.three = Key('three')
        self.four = Key('four')
        self.five = Key('five')
        self.six = Key('six')
        self.seven = Key('seven')
        self.eight = Key('eight')
        self.nine = Key('nine')
        self.colon = Key('colon')
        self.semicolon = Key('semicolon')
        self.less = Key('less')
        self.equal = Key('equal')
        self.greater = Key('greater')
        self.question = Key('question')
        self.at = Key('at')
        self.a = Key('a')
        self.b = Key('b')
        self.c = Key('c')
        self.d = Key('d')
        self.e = Key('e')
        self.f = Key('f')
        self.g = Key('g')
        self.h = Key('h')
        self.i = Key('i')
        self.j = Key('j')
        self.k = Key('k')
        self.l = Key('l')
        self.m = Key('m')
        self.n = Key('n')
        self.o = Key('o')
        self.p = Key('p')
        self.q = Key('q')
        self.r = Key('r')
        self.s = Key('s')
        self.t = Key('t')
        self.u = Key('u')
        self.v = Key('v')
        self.w = Key('w')
        self.x = Key('x')
        self.y = Key('y')
        self.z = Key('z')
        self.bracketLeft = Key('bracketLeft')
        self.backslash = Key('backslash')
        self.bracketRight = Key('bracketRight')
        self.asciiCircum = Key('asciiCircum')
        self.underscore = Key('underscore')
        self.quoteLeft = Key('quoteLeft')
        self.braceLeft = Key('braceLeft')
        self.bar = Key('bar')
        self.braceRight = Key('braceRight')
        self.asciiTilde = Key('asciiTilde')
        self.nobreakspace = Key('nobreakspace')
        self.exclamdown = Key('exclamdown')
        self.cent = Key('cent')
        self.sterling = Key('sterling')
        self.currency = Key('currency')
        self.yen = Key('yen')
        self.brokenbar = Key('brokenbar')
        self.section = Key('section')
        self.diaeresis = Key('diaeresis')
        self.copyright = Key('copyright')
        self.ordfeminine = Key('ordfeminine')
        self.guillemotleft = Key('guillemotleft')
        self.notsign = Key('notsign')
        self.hyphen = Key('hyphen')
        self.registered = Key('registered')
        self.macron = Key('macron')
        self.degree = Key('degree')
        self.plusminus = Key('plusminus')
        self.twosuperior = Key('twosuperior')
        self.threesuperior = Key('threesuperior')
        self.acute = Key('acute')
        self.mu = Key('mu')
        self.paragraph = Key('paragraph')
        self.periodcentered = Key('periodcentered')
        self.cedilla = Key('cedilla')
        self.onesuperior = Key('onesuperior')
        self.masculine = Key('masculine')
        self.guillemotright = Key('guillemotright')
        self.onequarter = Key('onequarter')
        self.onehalf = Key('onehalf')
        self.threequarters = Key('threequarters')
        self.questiondown = Key('questiondown')
        self.agrave = Key('agrave')
        self.aacute = Key('aacute')
        self.acircumflex = Key('acircumflex')
        self.atilde = Key('atilde')
        self.adiaeresis = Key('adiaeresis')
        self.aring = Key('aring')
        self.aE = Key('aE')
        self.ccedilla = Key('ccedilla')
        self.egrave = Key('egrave')
        self.eacute = Key('eacute')
        self.ecircumflex = Key('ecircumflex')
        self.ediaeresis = Key('ediaeresis')
        self.igrave = Key('igrave')
        self.iacute = Key('iacute')
        self.icircumflex = Key('icircumflex')
        self.idiaeresis = Key('idiaeresis')
        self.eTH = Key('eTH')
        self.ntilde = Key('ntilde')
        self.ograve = Key('ograve')
        self.oacute = Key('oacute')
        self.ocircumflex = Key('ocircumflex')
        self.otilde = Key('otilde')
        self.odiaeresis = Key('odiaeresis')
        self.multiply = Key('multiply')
        self.ooblique = Key('ooblique')
        self.ugrave = Key('ugrave')
        self.uacute = Key('uacute')
        self.ucircumflex = Key('ucircumflex')
        self.udiaeresis = Key('udiaeresis')
        self.yacute = Key('yacute')
        self.tHORN = Key('tHORN')
        self.ssharp = Key('ssharp')
        self.division = Key('division')
        self.ydiaeresis = Key('ydiaeresis')
        self.multi_key = Key('multi_key')
        self.codeinput = Key('codeinput')
        self.singleCandidate = Key('singleCandidate')
        self.multipleCandidate = Key('multipleCandidate')
        self.previousCandidate = Key('previousCandidate')
        self.mode_switch = Key('mode_switch')
        self.kanji = Key('kanji')
        self.muhenkan = Key('muhenkan')
        self.henkan = Key('henkan')
        self.romaji = Key('romaji')
        self.hiragana = Key('hiragana')
        self.katakana = Key('katakana')
        self.hiragana_Katakana = Key('hiragana_Katakana')
        self.zenkaku = Key('zenkaku')
        self.hankaku = Key('hankaku')
        self.zenkaku_Hankaku = Key('zenkaku_Hankaku')
        self.touroku = Key('touroku')
        self.massyo = Key('massyo')
        self.kana_Lock = Key('kana_Lock')
        self.kana_Shift = Key('kana_Shift')
        self.eisu_Shift = Key('eisu_Shift')
        self.eisu_toggle = Key('eisu_toggle')
        self.hangul = Key('hangul')
        self.hangul_Start = Key('hangul_Start')
        self.hangul_End = Key('hangul_End')
        self.hangul_Hanja = Key('hangul_Hanja')
        self.hangul_Jamo = Key('hangul_Jamo')
        self.hangul_Romaja = Key('hangul_Romaja')
        self.hangul_Jeonja = Key('hangul_Jeonja')
        self.hangul_Banja = Key('hangul_Banja')
        self.hangul_PreHanja = Key('hangul_PreHanja')
        self.hangul_PostHanja = Key('hangul_PostHanja')
        self.hangul_Special = Key('hangul_Special')
        self.dead_Grave = Key('dead_Grave')
        self.dead_Acute = Key('dead_Acute')
        self.dead_Circumflex = Key('dead_Circumflex')
        self.dead_Tilde = Key('dead_Tilde')
        self.dead_Macron = Key('dead_Macron')
        self.dead_Breve = Key('dead_Breve')
        self.dead_Abovedot = Key('dead_Abovedot')
        self.dead_Diaeresis = Key('dead_Diaeresis')
        self.dead_Abovering = Key('dead_Abovering')
        self.dead_Doubleacute = Key('dead_Doubleacute')
        self.dead_Caron = Key('dead_Caron')
        self.dead_Cedilla = Key('dead_Cedilla')
        self.dead_Ogonek = Key('dead_Ogonek')
        self.dead_Iota = Key('dead_Iota')
        self.dead_Voiced_Sound = Key('dead_Voiced_Sound')
        self.dead_Semivoiced_Sound = Key('dead_Semivoiced_Sound')
        self.dead_Belowdot = Key('dead_Belowdot')
        self.dead_Hook = Key('dead_Hook')
        self.dead_Horn = Key('dead_Horn')
        self.back = Key('back')
        self.forward = Key('forward')
        self.stop = Key('stop')
        self.refresh = Key('refresh')
        self.volumeDown = Key('volumeDown')
        self.volumeMute = Key('volumeMute')
        self.volumeUp = Key('volumeUp')
        self.bassBoost = Key('bassBoost')
        self.bassUp = Key('bassUp')
        self.bassDown = Key('bassDown')
        self.trebleUp = Key('trebleUp')
        self.trebleDown = Key('trebleDown')
        self.mediaPlay = Key('mediaPlay') # A key setting the state of the media player to play
        self.mediaStop = Key('mediaStop') # A key setting the state of the media player to stop
        self.mediaPrevious = Key('mediaPrevious')
        self.mediaNext = Key('mediaNext')
        self.mediaRecord = Key('mediaRecord')
        self.mediaPause = Key('mediaPause') # A key setting the state of the media player to pause (Note: not the pause/break key)
        self.mediaTogglePlayPause = Key('mediaTogglePlayPause') # A key to toggle the play/pause state in the media player (rather than setting an absolute state)
        self.homePage = Key('homePage')
        self.favorites = Key('favorites')
        self.search = Key('search')
        self.standby = Key('standby')
        self.openUrl = Key('openUrl')
        self.launchMail = Key('launchMail')
        self.launchMedia = Key('launchMedia')
        self.launch0 = Key('launch0') # On X11 this key is mapped to "My Computer" (XF86XK_MyComputer) key for legacy reasons.
        self.launch1 = Key('launch1') # On X11 this key is mapped to "Calculator" (XF86XK_Calculator) key for legacy reasons.
        self.launch2 = Key('launch2') # On X11 this key is mapped to XF86XK_Launch0 key for legacy reasons.
        self.launch3 = Key('launch3') # On X11 this key is mapped to XF86XK_Launch1 key for legacy reasons.
        self.launch4 = Key('launch4') # On X11 this key is mapped to XF86XK_Launch2 key for legacy reasons.
        self.launch5 = Key('launch5') # On X11 this key is mapped to XF86XK_Launch3 key for legacy reasons.
        self.launch6 = Key('launch6') # On X11 this key is mapped to XF86XK_Launch4 key for legacy reasons.
        self.launch7 = Key('launch7') # On X11 this key is mapped to XF86XK_Launch5 key for legacy reasons.
        self.launch8 = Key('launch8') # On X11 this key is mapped to XF86XK_Launch6 key for legacy reasons.
        self.launch9 = Key('launch9') # On X11 this key is mapped to XF86XK_Launch7 key for legacy reasons.
        self.launchA = Key('launchA') # On X11 this key is mapped to XF86XK_Launch8 key for legacy reasons.
        self.launchB = Key('launchB') # On X11 this key is mapped to XF86XK_Launch9 key for legacy reasons.
        self.launchC = Key('launchC') # On X11 this key is mapped to XF86XK_LaunchA key for legacy reasons.
        self.launchD = Key('launchD') # On X11 this key is mapped to XF86XK_LaunchB key for legacy reasons.
        self.launchE = Key('launchE') # On X11 this key is mapped to XF86XK_LaunchC key for legacy reasons.
        self.launchF = Key('launchF') # On X11 this key is mapped to XF86XK_LaunchD key for legacy reasons.
        self.launchG = Key('launchG') # On X11 this key is mapped to XF86XK_LaunchE key for legacy reasons.
        self.launchH = Key('launchH') # On X11 this key is mapped to XF86XK_LaunchF key for legacy reasons.
        self.monBrightnessUp = Key('monBrightnessUp')
        self.monBrightnessDown = Key('monBrightnessDown')
        self.keyboardLightOnOff = Key('keyboardLightOnOff')
        self.keyboardBrightnessUp = Key('keyboardBrightnessUp')
        self.keyboardBrightnessDown = Key('keyboardBrightnessDown')
        self.powerOff = Key('powerOff')
        self.wakeUp = Key('wakeUp')
        self.eject = Key('eject')
        self.screenSaver = Key('screenSaver')
        self.wWW = Key('wWW')
        self.memo = Key('memo')
        self.lightBulb = Key('lightBulb')
        self.shop = Key('shop')
        self.history = Key('history')
        self.addFavorite = Key('addFavorite')
        self.hotLinks = Key('hotLinks')
        self.brightnessAdjust = Key('brightnessAdjust')
        self.finance = Key('finance')
        self.community = Key('community')
        self.audioRewind = Key('audioRewind')
        self.backForward = Key('backForward')
        self.applicationLeft = Key('applicationLeft')
        self.applicationRight = Key('applicationRight')
        self.book = Key('book')
        self.cD = Key('cD')
        self.calculator = Key('calculator') # On X11 this key is not mapped for legacy reasons. Use Qt.Key_Launch1 instead.
        self.toDoList = Key('toDoList')
        self.clearGrab = Key('clearGrab')
        self.close = Key('close')
        self.copy = Key('copy')
        self.cut = Key('cut')
        self.display = Key('display')
        self.dOS = Key('dOS')
        self.documents = Key('documents')
        self.excel = Key('excel')
        self.explorer = Key('explorer')
        self.game = Key('game')
        self.go = Key('go')
        self.iTouch = Key('iTouch')
        self.logOff = Key('logOff')
        self.market = Key('market')
        self.meeting = Key('meeting')
        self.menuKB = Key('menuKB')
        self.menuPB = Key('menuPB')
        self.mySites = Key('mySites')
        self.news = Key('news')
        self.officeHome = Key('officeHome')
        self.option = Key('option')
        self.paste = Key('paste')
        self.phone = Key('phone')
        self.calendar = Key('calendar')
        self.reply = Key('reply')
        self.reload = Key('reload')
        self.rotateWindows = Key('rotateWindows')
        self.rotationPB = Key('rotationPB')
        self.rotationKB = Key('rotationKB')
        self.save = Key('save')
        self.send = Key('send')
        self.spell = Key('spell')
        self.splitScreen = Key('splitScreen')
        self.support = Key('support')
        self.taskPane = Key('taskPane')
        self.terminal = Key('terminal')
        self.tools = Key('tools')
        self.travel = Key('travel')
        self.video = Key('video')
        self.word = Key('word')
        self.xfer = Key('xfer')
        self.zoomIn = Key('zoomIn')
        self.zoomOut = Key('zoomOut')
        self.away = Key('away')
        self.messenger = Key('messenger')
        self.webCam = Key('webCam')
        self.mailForward = Key('mailForward')
        self.pictures = Key('pictures')
        self.music = Key('music')
        self.battery = Key('battery')
        self.bluetooth = Key('bluetooth')
        self.wLAN = Key('wLAN')
        self.uWB = Key('uWB')
        self.audioForward = Key('audioForward')
        self.audioRepeat = Key('audioRepeat')
        self.audioRandomPlay = Key('audioRandomPlay')
        self.subtitle = Key('subtitle')
        self.audioCycleTrack = Key('audioCycleTrack')
        self.time = Key('time')
        self.hibernate = Key('hibernate')
        self.view = Key('view')
        self.topMenu = Key('topMenu')
        self.powerDown = Key('powerDown')
        self.suspend = Key('suspend')
        self.contrastAdjust = Key('contrastAdjust')
        self.mediaLast = Key('mediaLast')
        self.unknown = Key('unknown')
        self.call = Key('call') # A key to answer or initiate a call (see Qt.Key_ToggleCallHangup for a key to toggle current call state)
        self.camera = Key('camera') # A key to activate the camera shutter
        self.cameraFocus = Key('cameraFocus') # A key to focus the camera
        self.context1 = Key('context1')
        self.context2 = Key('context2')
        self.context3 = Key('context3')
        self.context4 = Key('context4')
        self.flip = Key('flip')
        self.hangup = Key('hangup') # A key to end an ongoing call (see Qt.Key_ToggleCallHangup for a key to toggle current call state)
        self.no = Key('no')
        self.select = Key('select')
        self.yes = Key('yes')
        self.toggleCallHangup = Key('toggleCallHangup') # A key to toggle the current call state (ie. either answer, or hangup) depending on current call state
        self.voiceDial = Key('voiceDial')
        self.lastNumberRedial = Key('lastNumberRedial')
        self.execute = Key('execute')
        self.printer = Key('printer')
        self.play = Key('play')
        self.sleep = Key('sleep')
        self.zoom = Key('zoom')
        self.cancel = Key('cancel')
        self.anykey = AnyKey(key for key in vars(self).values() if type(key) == Key)

    def _onkeyevent(self, keycode, isdown, eventargs):
        try:
            key = {
                0x01000000: self.escape,
                0x01000001: self.tab,
                0x01000002: self.backtab,
                0x01000003: self.backspace,
                0x01000004: self.enter,
                0x01000005: self.numpad_enter,
                0x01000006: self.insert,
                0x01000007: self.delete,
                0x01000008: self.pause,
                0x01000009: self.print_screen,
                0x0100000a: self.sysReq,
                0x0100000b: self.clear,
                0x01000010: self.home,
                0x01000011: self.end,
                0x01000012: self.left,
                0x01000013: self.up,
                0x01000014: self.right,
                0x01000015: self.down,
                0x01000016: self.pageUp,
                0x01000017: self.pageDown,
                0x01000020: self.shift,
                0x01000021: self.control,
                0x01000022: self.meta,
                0x01000023: self.alt,
                0x01001103: self.altGr,
                0x01000024: self.capsLock,
                0x01000025: self.numLock,
                0x01000026: self.scrollLock,
                0x01000030: self.f1,
                0x01000031: self.f2,
                0x01000032: self.f3,
                0x01000033: self.f4,
                0x01000034: self.f5,
                0x01000035: self.f6,
                0x01000036: self.f7,
                0x01000037: self.f8,
                0x01000038: self.f9,
                0x01000039: self.f10,
                0x0100003a: self.f11,
                0x0100003b: self.f12,
                0x0100003c: self.f13,
                0x0100003d: self.f14,
                0x0100003e: self.f15,
                0x0100003f: self.f16,
                0x01000040: self.f17,
                0x01000041: self.f18,
                0x01000042: self.f19,
                0x01000043: self.f20,
                0x01000044: self.f21,
                0x01000045: self.f22,
                0x01000046: self.f23,
                0x01000047: self.f24,
                0x01000048: self.f25,
                0x01000049: self.f26,
                0x0100004a: self.f27,
                0x0100004b: self.f28,
                0x0100004c: self.f29,
                0x0100004d: self.f30,
                0x0100004e: self.f31,
                0x0100004f: self.f32,
                0x01000050: self.f33,
                0x01000051: self.f34,
                0x01000052: self.f35,
                0x01000053: self.super_L,
                0x01000054: self.super_R,
                0x01000055: self.menu,
                0x01000056: self.hyper_L,
                0x01000057: self.hyper_R,
                0x01000058: self.help,
                0x01000059: self.direction_L,
                0x01000060: self.direction_R,
                0x20: self.space,
                0x21: self.exclam,
                0x22: self.quoteDbl,
                0x23: self.numberSign,
                0x24: self.dollar,
                0x25: self.percent,
                0x26: self.ampersand,
                0x27: self.apostrophe,
                0x28: self.parenLeft,
                0x29: self.parenRight,
                0x2a: self.asterisk,
                0x2b: self.plus,
                0x2c: self.comma,
                0x2d: self.minus,
                0x2e: self.period,
                0x2f: self.slash,
                0x30: self.zero,
                0x31: self.one,
                0x32: self.two,
                0x33: self.three,
                0x34: self.four,
                0x35: self.five,
                0x36: self.six,
                0x37: self.seven,
                0x38: self.eight,
                0x39: self.nine,
                0x3a: self.colon,
                0x3b: self.semicolon,
                0x3c: self.less,
                0x3d: self.equal,
                0x3e: self.greater,
                0x3f: self.question,
                0x40: self.at,
                0x41: self.a,
                0x42: self.b,
                0x43: self.c,
                0x44: self.d,
                0x45: self.e,
                0x46: self.f,
                0x47: self.g,
                0x48: self.h,
                0x49: self.i,
                0x4a: self.j,
                0x4b: self.k,
                0x4c: self.l,
                0x4d: self.m,
                0x4e: self.n,
                0x4f: self.o,
                0x50: self.p,
                0x51: self.q,
                0x52: self.r,
                0x53: self.s,
                0x54: self.t,
                0x55: self.u,
                0x56: self.v,
                0x57: self.w,
                0x58: self.x,
                0x59: self.y,
                0x5a: self.z,
                0x5b: self.bracketLeft,
                0x5c: self.backslash,
                0x5d: self.bracketRight,
                0x5e: self.asciiCircum,
                0x5f: self.underscore,
                0x60: self.quoteLeft,
                0x7b: self.braceLeft,
                0x7c: self.bar,
                0x7d: self.braceRight,
                0x7e: self.asciiTilde,
                0x0a0: self.nobreakspace,
                0x0a1: self.exclamdown,
                0x0a2: self.cent,
                0x0a3: self.sterling,
                0x0a4: self.currency,
                0x0a5: self.yen,
                0x0a6: self.brokenbar,
                0x0a7: self.section,
                0x0a8: self.diaeresis,
                0x0a9: self.copyright,
                0x0aa: self.ordfeminine,
                0x0ab: self.guillemotleft,
                0x0ac: self.notsign,
                0x0ad: self.hyphen,
                0x0ae: self.registered,
                0x0af: self.macron,
                0x0b0: self.degree,
                0x0b1: self.plusminus,
                0x0b2: self.twosuperior,
                0x0b3: self.threesuperior,
                0x0b4: self.acute,
                0x0b5: self.mu,
                0x0b6: self.paragraph,
                0x0b7: self.periodcentered,
                0x0b8: self.cedilla,
                0x0b9: self.onesuperior,
                0x0ba: self.masculine,
                0x0bb: self.guillemotright,
                0x0bc: self.onequarter,
                0x0bd: self.onehalf,
                0x0be: self.threequarters,
                0x0bf: self.questiondown,
                0x0c0: self.agrave,
                0x0c1: self.aacute,
                0x0c2: self.acircumflex,
                0x0c3: self.atilde,
                0x0c4: self.adiaeresis,
                0x0c5: self.aring,
                0x0c6: self.aE,
                0x0c7: self.ccedilla,
                0x0c8: self.egrave,
                0x0c9: self.eacute,
                0x0ca: self.ecircumflex,
                0x0cb: self.ediaeresis,
                0x0cc: self.igrave,
                0x0cd: self.iacute,
                0x0ce: self.icircumflex,
                0x0cf: self.idiaeresis,
                0x0d0: self.eTH,
                0x0d1: self.ntilde,
                0x0d2: self.ograve,
                0x0d3: self.oacute,
                0x0d4: self.ocircumflex,
                0x0d5: self.otilde,
                0x0d6: self.odiaeresis,
                0x0d7: self.multiply,
                0x0d8: self.ooblique,
                0x0d9: self.ugrave,
                0x0da: self.uacute,
                0x0db: self.ucircumflex,
                0x0dc: self.udiaeresis,
                0x0dd: self.yacute,
                0x0de: self.tHORN,
                0x0df: self.ssharp,
                0x0f7: self.division,
                0x0ff: self.ydiaeresis,
                0x01001120: self.multi_key,
                0x01001137: self.codeinput,
                0x0100113c: self.singleCandidate,
                0x0100113d: self.multipleCandidate,
                0x0100113e: self.previousCandidate,
                0x0100117e: self.mode_switch,
                0x01001121: self.kanji,
                0x01001122: self.muhenkan,
                0x01001123: self.henkan,
                0x01001124: self.romaji,
                0x01001125: self.hiragana,
                0x01001126: self.katakana,
                0x01001127: self.hiragana_Katakana,
                0x01001128: self.zenkaku,
                0x01001129: self.hankaku,
                0x0100112a: self.zenkaku_Hankaku,
                0x0100112b: self.touroku,
                0x0100112c: self.massyo,
                0x0100112d: self.kana_Lock,
                0x0100112e: self.kana_Shift,
                0x0100112f: self.eisu_Shift,
                0x01001130: self.eisu_toggle,
                0x01001131: self.hangul,
                0x01001132: self.hangul_Start,
                0x01001133: self.hangul_End,
                0x01001134: self.hangul_Hanja,
                0x01001135: self.hangul_Jamo,
                0x01001136: self.hangul_Romaja,
                0x01001138: self.hangul_Jeonja,
                0x01001139: self.hangul_Banja,
                0x0100113a: self.hangul_PreHanja,
                0x0100113b: self.hangul_PostHanja,
                0x0100113f: self.hangul_Special,
                0x01001250: self.dead_Grave,
                0x01001251: self.dead_Acute,
                0x01001252: self.dead_Circumflex,
                0x01001253: self.dead_Tilde,
                0x01001254: self.dead_Macron,
                0x01001255: self.dead_Breve,
                0x01001256: self.dead_Abovedot,
                0x01001257: self.dead_Diaeresis,
                0x01001258: self.dead_Abovering,
                0x01001259: self.dead_Doubleacute,
                0x0100125a: self.dead_Caron,
                0x0100125b: self.dead_Cedilla,
                0x0100125c: self.dead_Ogonek,
                0x0100125d: self.dead_Iota,
                0x0100125e: self.dead_Voiced_Sound,
                0x0100125f: self.dead_Semivoiced_Sound,
                0x01001260: self.dead_Belowdot,
                0x01001261: self.dead_Hook,
                0x01001262: self.dead_Horn,
                0x01000061: self.back,
                0x01000062: self.forward,
                0x01000063: self.stop,
                0x01000064: self.refresh,
                0x01000070: self.volumeDown,
                0x01000071: self.volumeMute,
                0x01000072: self.volumeUp,
                0x01000073: self.bassBoost,
                0x01000074: self.bassUp,
                0x01000075: self.bassDown,
                0x01000076: self.trebleUp,
                0x01000077: self.trebleDown,
                0x01000080: self.mediaPlay,
                0x01000081: self.mediaStop,
                0x01000082: self.mediaPrevious,
                0x01000083: self.mediaNext,
                0x01000084: self.mediaRecord,
                0x1000085: self.mediaPause,
                0x1000086: self.mediaTogglePlayPause,
                0x01000090: self.homePage,
                0x01000091: self.favorites,
                0x01000092: self.search,
                0x01000093: self.standby,
                0x01000094: self.openUrl,
                0x010000a0: self.launchMail,
                0x010000a1: self.launchMedia,
                0x010000a2: self.launch0,
                0x010000a3: self.launch1,
                0x010000a4: self.launch2,
                0x010000a5: self.launch3,
                0x010000a6: self.launch4,
                0x010000a7: self.launch5,
                0x010000a8: self.launch6,
                0x010000a9: self.launch7,
                0x010000aa: self.launch8,
                0x010000ab: self.launch9,
                0x010000ac: self.launchA,
                0x010000ad: self.launchB,
                0x010000ae: self.launchC,
                0x010000af: self.launchD,
                0x010000b0: self.launchE,
                0x010000b1: self.launchF,
                0x0100010e: self.launchG,
                0x0100010f: self.launchH,
                0x010000b2: self.monBrightnessUp,
                0x010000b3: self.monBrightnessDown,
                0x010000b4: self.keyboardLightOnOff,
                0x010000b5: self.keyboardBrightnessUp,
                0x010000b6: self.keyboardBrightnessDown,
                0x010000b7: self.powerOff,
                0x010000b8: self.wakeUp,
                0x010000b9: self.eject,
                0x010000ba: self.screenSaver,
                0x010000bb: self.wWW,
                0x010000bc: self.memo,
                0x010000bd: self.lightBulb,
                0x010000be: self.shop,
                0x010000bf: self.history,
                0x010000c0: self.addFavorite,
                0x010000c1: self.hotLinks,
                0x010000c2: self.brightnessAdjust,
                0x010000c3: self.finance,
                0x010000c4: self.community,
                0x010000c5: self.audioRewind,
                0x010000c6: self.backForward,
                0x010000c7: self.applicationLeft,
                0x010000c8: self.applicationRight,
                0x010000c9: self.book,
                0x010000ca: self.cD,
                0x010000cb: self.calculator,
                0x010000cc: self.toDoList,
                0x010000cd: self.clearGrab,
                0x010000ce: self.close,
                0x010000cf: self.copy,
                0x010000d0: self.cut,
                0x010000d1: self.display,
                0x010000d2: self.dOS,
                0x010000d3: self.documents,
                0x010000d4: self.excel,
                0x010000d5: self.explorer,
                0x010000d6: self.game,
                0x010000d7: self.go,
                0x010000d8: self.iTouch,
                0x010000d9: self.logOff,
                0x010000da: self.market,
                0x010000db: self.meeting,
                0x010000dc: self.menuKB,
                0x010000dd: self.menuPB,
                0x010000de: self.mySites,
                0x010000df: self.news,
                0x010000e0: self.officeHome,
                0x010000e1: self.option,
                0x010000e2: self.paste,
                0x010000e3: self.phone,
                0x010000e4: self.calendar,
                0x010000e5: self.reply,
                0x010000e6: self.reload,
                0x010000e7: self.rotateWindows,
                0x010000e8: self.rotationPB,
                0x010000e9: self.rotationKB,
                0x010000ea: self.save,
                0x010000eb: self.send,
                0x010000ec: self.spell,
                0x010000ed: self.splitScreen,
                0x010000ee: self.support,
                0x010000ef: self.taskPane,
                0x010000f0: self.terminal,
                0x010000f1: self.tools,
                0x010000f2: self.travel,
                0x010000f3: self.video,
                0x010000f4: self.word,
                0x010000f5: self.xfer,
                0x010000f6: self.zoomIn,
                0x010000f7: self.zoomOut,
                0x010000f8: self.away,
                0x010000f9: self.messenger,
                0x010000fa: self.webCam,
                0x010000fb: self.mailForward,
                0x010000fc: self.pictures,
                0x010000fd: self.music,
                0x010000fe: self.battery,
                0x010000ff: self.bluetooth,
                0x01000100: self.wLAN,
                0x01000101: self.uWB,
                0x01000102: self.audioForward,
                0x01000103: self.audioRepeat,
                0x01000104: self.audioRandomPlay,
                0x01000105: self.subtitle,
                0x01000106: self.audioCycleTrack,
                0x01000107: self.time,
                0x01000108: self.hibernate,
                0x01000109: self.view,
                0x0100010a: self.topMenu,
                0x0100010b: self.powerDown,
                0x0100010c: self.suspend,
                0x0100010d: self.contrastAdjust,
                0x0100ffff: self.mediaLast,
                0x01ffffff: self.unknown,
                0x01100004: self.call,
                0x01100020: self.camera,
                0x01100021: self.cameraFocus,
                0x01100000: self.context1,
                0x01100001: self.context2,
                0x01100002: self.context3,
                0x01100003: self.context4,
                0x01100006: self.flip,
                0x01100005: self.hangup,
                0x01010002: self.no,
                0x01010000: self.select,
                0x01010001: self.yes,
                0x01100007: self.toggleCallHangup,
                0x01100008: self.voiceDial,
                0x01100009: self.lastNumberRedial,
                0x01020003: self.execute,
                0x01020002: self.printer,
                0x01020005: self.play,
                0x01020004: self.sleep,
                0x01020006: self.zoom,
                0x01020001: self.cancel
            }[keycode]
        except KeyError:
            if isdown: print("Unknown keycode: " + str(keycode))
        else:
            key.isdown = isdown
            if isdown:
                key.send(eventargs)
