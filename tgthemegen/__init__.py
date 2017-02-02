from enum import Enum

from tgthemegen.generate import Color

__author__ = 'rawieo, ctyode'  # self.__пидор__('ты')


def clamp(a: float, rng_min: float=0.0, rng_max: float=1.0) -> float:
    return min(rng_max, max(rng_min, a))


class ColorSource(Enum):
    primary = 0
    accent = 1
    background = 2
    foreground = 3
    predefined = 4


class ColorProperty:
    def __init__(self, source: ColorSource, color: Color=None, transform=None):
        self.source = source
        self.color = color
        self.transform = transform

    def calculate(self, primary: Color, accent: Color, foreground: Color, background: Color) -> Color:
        channels = []
        if self.source is ColorSource.primary:
            channels = primary.channels
        elif self.source is ColorSource.accent:
            channels = accent.channels
        elif self.source is ColorSource.foreground:
            channels = foreground.channels
        elif self.source is ColorSource.background:
            channels = background.channels
        return Color.from_channels([c * t for c, t in zip(channels, self.transform)])

    @staticmethod
    def from_repr(r):
        source = None
        if r[0] == 'primary':
            source = ColorSource.primary
        if r[0] == 'accent':
            source = ColorSource.accent
        if r[0] == 'background':
            source = ColorSource.background
        if r[0] == 'foreground':
            source = ColorSource.foreground
        return ColorProperty(source=source, transform=r[1])


properties = {
    'windowBg': ColorProperty(source=ColorSource.background),
    'windowFg': ColorProperty(source=ColorSource.foreground),
    'windowBgOver': ColorProperty(source=ColorSource.background, transform='todo'),  # TODO
    'windowBgRipple': ColorProperty(source=ColorSource.background, transform='todo'),  # TODO
    'windowFgOver': 'windowFg',
    'windowSubTextFg': ColorProperty(source=ColorSource.foreground, transform='todo'),  # TODO
    'windowSubTextFgOver': ColorProperty(source=ColorSource.foreground, transform='todo'),  # TODO
    'windowBoldFg': ColorProperty(source=ColorSource.foreground, transform='todo'),  # TODO
    'windowBoldFgOver': 'windowBoldFg',
    'windowBgActive': ColorProperty(source=ColorSource.accent),  # TODO
    'windowFgActive': ColorProperty(source=ColorSource.foreground),  # TODO
    'windowActiveTextFg': ColorProperty(source=ColorSource.primary),
    'windowShadowFg': '#000000',
    'windowShadowFgFallback': '#f1f1f1',
    'shadowFg': '#00000018',
    'slideFadeOutBg': '#0000003c',
    'slideFadeOutShadowFg': 'windowShadowFg',
    'imageBg': '#000000',
    'imageBgTransparent': '#ffffff',
    'activeButtonBg': 'windowBgActive',
    'activeButtonBgOver': ColorProperty(source=ColorSource.accent, transform='todo'),  # TODO
    'activeButtonBgRipple': ColorProperty(source=ColorSource.accent, transform='todo'),  # TODO
    'activeButtonFg': 'windowFgActive',
    'activeButtonFgOver': 'activeButtonFg',
    'activeButtonSecondaryFg': ColorProperty(source=ColorSource.foreground, transform='todo'),
    'activeButtonSecondaryFgOver': 'activeButtonSecondaryFg',
    'activeLineFg': ColorProperty(source=ColorSource.primary),  # TODO
    'activeLineFgError': '#cc434c',
    'lightButtonBg': 'windowBg',
    'lightButtonBgOver': '#fef1f1',
    'lightButtonBgRipple': '#fde3e3',
    'lightButtonFg': 'windowActiveTextFg',
    'lightButtonFgOver': 'lightButtonFg',
    'attentionButtonFg': '#d14e4e',
    'attentionButtonFgOver': '#d14e4e',
    'attentionButtonBgOver': '#fcdfde',
    'attentionButtonBgRipple': '#f4c3c2',
    'outlineButtonBg': 'windowBg',
    'outlineButtonBgOver': 'lightButtonBgOver',
    'outlineButtonOutlineFg': 'windowBgActive',
    'outlineButtonBgRipple': 'lightButtonBgRipple',
    'menuBg': 'windowBg',
    'menuBgOver': 'windowBgOver',
    'menuBgRipple': 'windowBgRipple',
    'menuIconFg': '#a8a8a8',
    'menuIconFgOver': '#999999',
    'menuSubmenuArrowFg': '#373737',
    'menuFgDisabled': '#cccccc',
    'menuSeparatorFg': '#f1f1f1',
    'scrollBarBg': '#00000053',
    'scrollBarBgOver': '#0000007a',
    'scrollBg': '#00000000',
    'scrollBgOver': '#0000001a',
    'smallCloseIconFg': '#c7c7c7',
    'smallCloseIconFgOver': '#a3a3a3',
    'radialFg': 'windowFgActive',
    'radialBg': '#00000056',
    'placeholderFg': 'windowSubTextFg',
    'placeholderFgActive': '#aaaaaa',
    'inputBorderFg': '#e0e0e0',
    'filterInputBorderFg': '#e34053',
    'checkboxFg': '#b3b3b3',
    'sliderBgInactive': '#e1eaef',
    'sliderBgActive': 'windowBgActive',
    'tooltipBg': '#eef2f5',
    'tooltipFg': '#5d6c80',
    'tooltipBorderFg': '#c9d1db',
    'titleBg': 'windowBgOver',
    'titleShadow': '#00000003',
    'titleButtonFg': '#ababab',
    'titleButtonBgOver': '#e5e5e5',
    'titleButtonFgOver': '#9a9a9a',
    'titleButtonCloseBgOver': '#e81123',
    'titleButtonCloseFgOver': 'windowFgActive',
    'titleFgActive': '#3e3c3e',
    'titleFg': '#acacac',
    'trayCounterBg': '#f23c34',
    'trayCounterBgMute': '#888888',
    'trayCounterFg': '#ffffff',
    'trayCounterBgMacInvert': '#ffffff',
    'trayCounterFgMacInvert': '#ffffff01',
    'layerBg': '#0000007f',
    'cancelIconFg': 'menuIconFg',
    'cancelIconFgOver': 'menuIconFgOver',
    'boxBg': 'windowBg',
    'boxTextFg': 'windowFg',
    'boxTextFgGood': '#4ab44a',
    'boxTextFgError': '#d84d4d',
    'boxTitleFg': '#404040',
    'boxSearchBg': 'boxBg',
    'boxSearchCancelIconFg': 'cancelIconFg',
    'boxSearchCancelIconFgOver': 'cancelIconFgOver',
    'boxTitleAdditionalFg': '#808080',
    'boxTitleCloseFg': 'cancelIconFg',
    'boxTitleCloseFgOver': 'cancelIconFgOver',
    'membersAboutLimitFg': 'windowSubTextFgOver',
    'contactsBg': 'windowBg',
    'contactsBgOver': 'windowBgOver',
    'contactsNameFg': 'boxTextFg',
    'contactsStatusFg': 'windowSubTextFg',
    'contactsStatusFgOver': 'windowSubTextFgOver',
    'contactsStatusFgOnline': 'windowActiveTextFg',
    'photoCropFadeBg': 'layerBg',
    'photoCropPointFg': '#ffffff7f',
    'introBg': 'windowBg',
    'introTitleFg': 'windowBoldFg',
    'introDescriptionFg': 'windowSubTextFg',
    'introErrorFg': 'windowSubTextFg',
    'introCoverTopBg': '#0f89d0',
    'introCoverBottomBg': '#39b0f0',
    'introCoverIconsFg': '#5ec6ff',
    'introCoverPlaneTrace': '#5ec6ff69',
    'introCoverPlaneInner': '#c6d8e8',
    'introCoverPlaneOuter': '#a1bed4',
    'introCoverPlaneTop': '#ffffff',
    'dialogsMenuIconFg': 'menuIconFg',
    'dialogsMenuIconFgOver': 'menuIconFgOver',
    'dialogsBg': 'windowBg',
    'dialogsNameFg': 'windowBoldFg',
    'dialogsChatIconFg': 'dialogsNameFg',
    'dialogsDateFg': 'windowSubTextFg',
    'dialogsTextFg': 'windowSubTextFg',
    'dialogsTextFgService': 'windowActiveTextFg',
    'dialogsDraftFg': '#dd4b39',
    'dialogsVerifiedIconBg': 'windowBgActive',
    'dialogsVerifiedIconFg': 'windowFgActive',
    'dialogsSendingIconFg': '#c1c1c1',
    'dialogsSentIconFg': '#a8a8a8',
    'dialogsUnreadBg': 'windowBgActive',
    'dialogsUnreadBgMuted': '#F2B0B8',
    'dialogsUnreadFg': 'windowFgActive',
    'dialogsBgOver': 'windowBgOver',
    'dialogsNameFgOver': 'windowBoldFgOver',
    'dialogsChatIconFgOver': 'dialogsNameFgOver',
    'dialogsDateFgOver': 'windowSubTextFgOver',
    'dialogsTextFgOver': 'windowSubTextFgOver',
    'dialogsTextFgServiceOver': 'dialogsTextFgService',
    'dialogsDraftFgOver': 'dialogsDraftFg',
    'dialogsVerifiedIconBgOver': 'dialogsVerifiedIconBg',
    'dialogsVerifiedIconFgOver': 'dialogsVerifiedIconFg',
    'dialogsSendingIconFgOver': 'dialogsSendingIconFg',
    'dialogsSentIconFgOver': 'dialogsSentIconFg',
    'dialogsUnreadBgOver': 'dialogsUnreadBg',
    'dialogsUnreadBgMutedOver': 'dialogsUnreadBgMuted',
    'dialogsUnreadFgOver': 'dialogsUnreadFg',
    'dialogsBgActive': '#f77375',
    'dialogsNameFgActive': 'windowFgActive',
    'dialogsChatIconFgActive': 'dialogsNameFgActive',
    'dialogsDateFgActive': 'windowFgActive',
    'dialogsTextFgActive': 'windowFgActive',
    'dialogsTextFgServiceActive': 'dialogsTextFgActive',
    'dialogsDraftFgActive': '#ffffff',
    'dialogsVerifiedIconBgActive': 'dialogsTextFgActive',
    'dialogsVerifiedIconFgActive': 'dialogsBgActive',
    'dialogsSendingIconFgActive': '#ffffff99',
    'dialogsSentIconFgActive': 'dialogsTextFgActive',
    'dialogsUnreadBgActive': 'dialogsTextFgActive',
    'dialogsUnreadBgMutedActive': 'dialogsDraftFgActive',
    'dialogsUnreadFgActive': 'dialogsBgActive',
    'dialogsForwardBg': 'dialogsBgActive',
    'dialogsForwardFg': 'dialogsNameFgActive',
    'searchedBarBg': 'windowBgOver',
    'searchedBarBorder': 'shadowFg',
    'searchedBarFg': 'windowSubTextFgOver',
    'topBarBg': 'windowBg',
    'emojiPanBg': 'windowBg',
    'emojiPanCategories': '#f7f7f7',
    'emojiPanHeaderFg': 'windowSubTextFg',
    'emojiPanHeaderBg': '#fffffff2',
    'stickerPanDeleteBg': '#000000cc',
    'stickerPanDeleteFg': 'windowFgActive',
    'stickerPreviewBg': '#ffffffb0',
    'historyTextInFg': 'windowFg',
    'historyTextOutFg': 'windowBg',
    'historyCaptionInFg': 'historyTextInFg',
    'historyCaptionOutFg': 'historyTextOutFg',
    'historyFileNameInFg': 'historyTextInFg',
    'historyFileNameOutFg': 'historyTextOutFg',
    'historyOutIconFg': '#F6133E',
    'historyOutIconFgSelected': '#ffffff',
    'historyIconFgInverted': 'windowFgActive',
    'historySendingOutIconFg': '#9dc2d9',
    'historySendingInIconFg': '#a0adb5',
    'historySendingInvertedIconFg': '#ffffffc8',
    'historySystemBg': '#89a0b47f',
    'historySystemBgSelected': '#bbc8d4a2',
    'historySystemFg': 'windowFgActive',
    'historyUnreadBarBg': '#fcfbfa',
    'historyUnreadBarBorder': 'shadowFg',
    'historyUnreadBarFg': '#538bb4',
    'historyForwardChooseBg': '#0000004c',
    'historyForwardChooseFg': 'windowFgActive',
    'historyPeer1NameFg': '#c03d33',
    'historyPeer1UserpicBg': '#e17076',
    'historyPeer2NameFg': '#4fad2d',
    'historyPeer2UserpicBg': '#7bc862',
    'historyPeer3NameFg': '#d09306',
    'historyPeer3UserpicBg': '#e5ca77',
    'historyPeer4NameFg': 'windowActiveTextFg',
    'historyPeer4UserpicBg': '#65aadd',
    'historyPeer5NameFg': '#8544d6',
    'historyPeer5UserpicBg': '#a695e7',
    'historyPeer6NameFg': '#cd4073',
    'historyPeer6UserpicBg': '#ee7aae',
    'historyPeer7NameFg': '#2996ad',
    'historyPeer7UserpicBg': '#6ec9cb',
    'historyPeer8NameFg': '#ce671b',
    'historyPeer8UserpicBg': '#faa774',
    'historyPeerUserpicFg': 'windowFgActive',
    'historyScrollBarBg': '#00000040',
    'historyScrollBarBgOver': '#00000053',
    'historyScrollBg': '#00000000',
    'historyScrollBgOver': '#0000001a',
    'msgInBg': 'windowBg',
    'msgInBgSelected': '#c2dcf2',
    'msgOutBg': '#ff99a5',
    'msgOutBgSelected': '#faa7a8',
    'msgSelectOverlay': '#358cd44c',
    'msgStickerOverlay': '#358cd47f',
    'msgInServiceFg': 'windowActiveTextFg',
    'msgInServiceFgSelected': 'windowActiveTextFg',
    'msgOutServiceFg': 'windowActiveTextFg',
    'msgOutServiceFgSelected': 'windowActiveTextFg',
    'msgInShadow': '#748ea229',
    'msgInShadowSelected': '#548dbb29',
    'msgOutShadow': '#748ea229',
    'msgOutShadowSelected': '#548dbb29',
    'msgInDateFg': '#c1c1c1',
    'msgInDateFgSelected': '#6a9cc5',
    'msgOutDateFg': '#ffffff',
    'msgOutDateFgSelected': '#a0acb6',
    'msgServiceFg': 'windowFgActive',
    'msgServiceBg': '#00558059',
    'msgServiceBgSelected': '#62afdda2',
    'msgInReplyBarColor': 'activeLineFg',
    'msgInReplyBarSelColor': 'activeLineFg',
    'msgOutReplyBarColor': 'historyOutIconFg',
    'msgOutReplyBarSelColor': 'historyOutIconFgSelected',
    'msgImgReplyBarColor': 'msgServiceFg',
    'msgInMonoFg': '#4e7391',
    'msgOutMonoFg': '#4e7391',
    'msgDateImgFg': 'msgServiceFg',
    'msgDateImgBg': '#00000054',
    'msgDateImgBgOver': '#00000074',
    'msgDateImgBgSelected': '#1c4a7187',
    'msgFileThumbLinkInFg': 'lightButtonFg',
    'msgFileThumbLinkInFgSelected': 'lightButtonFgOver',
    'msgFileThumbLinkOutFg': 'lightButtonFg',
    'msgFileThumbLinkOutFgSelected': 'lightButtonFgOver',
    'msgFileInBg': 'windowBgActive',
    'msgFileInBgOver': '#4eade3',
    'msgFileInBgSelected': '#FFFFFF',
    'msgFileOutBg': '#ffffff',
    'msgFileOutBgOver': '#ffffff',
    'msgFileOutBgSelected': '#ffffff',
    'msgFile1Bg': '#ffffff',
    'msgFile1BgDark': '#ffffff',
    'msgFile1BgOver': '#5294c4',
    'msgFile1BgSelected': '#5099d0',
    'msgFile2Bg': '#61b96e',
    'msgFile2BgDark': '#4da859',
    'msgFile2BgOver': '#44a050',
    'msgFile2BgSelected': '#46a07e',
    'msgFile3Bg': '#e47272',
    'msgFile3BgDark': '#cd5b5e',
    'msgFile3BgOver': '#c35154',
    'msgFile3BgSelected': '#9f6a82',
    'msgFile4Bg': '#efc274',
    'msgFile4BgDark': '#e6a561',
    'msgFile4BgOver': '#dc9c5a',
    'msgFile4BgSelected': '#b19d84',
    'msgWaveformInActive': '#windowBgActive',
    'msgWaveformInActiveSelected': '#51a3d3',
    'msgWaveformInInactive': '#d4dee6',
    'msgWaveformInInactiveSelected': '#9cc1e1',
    'msgWaveformOutActive': '#ffffff',
    'msgWaveformOutActiveSelected': 'e34053',
    'msgWaveformOutInactive': '#f77375',
    'msgWaveformOutInactiveSelected': '#ffffff',
    'msgBotKbOverBgAdd': '#ffffff20',
    'msgBotKbIconFg': 'msgServiceFg',
    'msgBotKbRippleBg': '#00000020',
    'mediaInFg': 'msgInDateFg',
    'mediaInFgSelected': 'msgInDateFgSelected',
    'mediaOutFg': 'msgOutDateFg',
    'mediaOutFgSelected': 'msgOutDateFgSelected',
    'youtubePlayIconBg': '#e83131c8',
    'youtubePlayIconFg': 'windowFgActive',
    'videoPlayIconBg': '#0000007f',
    'videoPlayIconFg': '#ffffff',
    'toastBg': '#000000b2',
    'toastFg': 'windowFgActive',
    'reportSpamBg': 'emojiPanHeaderBg',
    'reportSpamFg': 'windowFg',
    'historyToDownShadow': '#00000040',
    'historyComposeAreaBg': 'msgInBg',
    'historyComposeAreaFg': 'historyTextInFg',
    'historyComposeAreaFgService': 'msgInDateFg',
    'historyComposeIconFg': 'menuIconFg',
    'historyComposeIconFgOver': 'menuIconFgOver',
    'historySendIconFg': 'windowBgActive',
    'historySendIconFgOver': 'windowBgActive',
    'historyPinnedBg': 'historyComposeAreaBg',
    'historyReplyBg': 'historyComposeAreaBg',
    'historyReplyCancelFg': 'cancelIconFg',
    'historyReplyCancelFgOver': 'cancelIconFgOver',
    'historyComposeButtonBg': 'historyComposeAreaBg',
    'historyComposeButtonBgOver': 'windowBgOver',
    'historyComposeButtonBgRipple': 'windowBgRipple',
    'overviewCheckBg': '#00000040',
    'overviewCheckFg': 'windowBg',
    'overviewCheckFgActive': 'windowBg',
    'overviewPhotoSelectOverlay': '#40ace333',
    'profileStatusFgOver': '#7c99b2',
    'notificationsBoxMonitorFg': 'windowFg',
    'notificationsBoxScreenBg': 'dialogsBgActive',
    'notificationSampleUserpicFg': 'windowBgActive',
    'notificationSampleCloseFg': '#d7d7d7',
    'notificationSampleTextFg': '#d7d7d7',
    'notificationSampleNameFg': '#939393',
    'mainMenuBg': 'windowBg',
    'mainMenuCoverBg': 'dialogsBgActive',
    'mainMenuCoverFg': 'windowFgActive',
    'mediaPlayerBg': 'windowBg',
    'mediaPlayerActiveFg': 'windowBgActive',
    'mediaPlayerInactiveFg': 'sliderBgInactive',
    'mediaPlayerDisabledFg': '#9dd1ef',
    'mediaviewFileBg': 'windowBg',
    'mediaviewFileNameFg': 'windowFg',
    'mediaviewFileSizeFg': 'windowSubTextFg',
    'mediaviewFileRedCornerFg': '#d55959',
    'mediaviewFileYellowCornerFg': '#e8a659',
    'mediaviewFileGreenCornerFg': '#49a957',
    'mediaviewFileBlueCornerFg': '#599dcf',
    'mediaviewFileExtFg': 'activeButtonFg',
    'mediaviewMenuBg': '#383838',
    'mediaviewMenuBgOver': '#505050',
    'mediaviewMenuBgRipple': '#676767',
    'mediaviewMenuFg': 'windowFgActive',
    'mediaviewBg': '#222222eb',
    'mediaviewVideoBg': 'imageBg',
    'mediaviewControlBg': '#0000003c',
    'mediaviewControlFg': 'windowFgActive',
    'mediaviewCaptionBg': '#11111180',
    'mediaviewCaptionFg': 'mediaviewControlFg',
    'mediaviewTextLinkFg': '#ffffff',
    'mediaviewSaveMsgBg': 'toastBg',
    'mediaviewSaveMsgFg': 'toastFg',
    'mediaviewPlaybackActive': '#c7c7c7',
    'mediaviewPlaybackInactive': '#252525',
    'mediaviewPlaybackActiveOver': '#ffffff',
    'mediaviewPlaybackInactiveOver': '#474747',
    'mediaviewPlaybackProgressFg': '#ffffffc7',
    'mediaviewPlaybackIconFg': 'mediaviewPlaybackActive',
    'mediaviewPlaybackIconFgOver': 'mediaviewPlaybackActiveOver',
    'mediaviewTransparentBg': '#ffffff',
    'mediaviewTransparentFg': '#cccccc',
    'notificationBg': 'windowBg'}
