FEATURES_CUSTOM_CALLBACK = {
  'global_namespace' : str,
  'global_ttl' : int,
  'policiesByServerPoolFeature' : bool,
  'messagesBySecFeature' : bool,
  'messagesBySecStoreDays' : int,
  'feederFeaturesEnabled' : bool,
  'fallbackToNonPoolPolicies' : bool,
  'featuresByServerPool' : bool,
  'learnFeature' : bool,
  'learnPredictSafeValue' : float,
  'learnOnlyOnce' : bool,
  'learnEscalationValue' : float,
  'learnTimeFrameValue' : list,
  'learnBlockMinutes' : float,
  'spfStrictRejectFeature' : bool,
  'rateReputationFeature' : bool,
  'rateReputationBlockHitValue' : int,
  'rateReputationDecreaseValue' : float,
  'rateReputationIncreaseMinutes' : float,
  'ipReputationFeature' : bool,
  'ipReputationHitValue' : int,
  'ipReputationDecreaseValue' : float,
  'ipReputationIncreaseMinutes' : float,
  'subjectReputationFeature' : bool,
  'subjectReputationHitValue' : int,
  'subjectReputationDecreaseValue' : float,
  'subjectReputationIncreaseMinutes' : float,
  'global_conditions' : list,
  'global_custom_block' : int
}

METADATA_CUSTOM_CALLBACK = {
  'learnPredictSafeValue' : float,
  'learnEscalationValue' : float,
  'subject_repeated_count' : int,
  'ip_reputation_lastupdate' : float,
  'subject_lastupdate' : float,
  'sentmessages_lastupdate' : float,
  'last_update' : float,
  'last_subject' : str,
  'blue_creation_date' : float,
  'block_count' : int,
  'learningBlueMode' : bool,
  'learningRedMode' : bool,
  'manual_block' : bool,
  'predictBy' : str,
  'bypass' : bool
}

POLICY_CUSTOM_CALLBACK = {
  'enable' : bool,
  'stophere' : bool,
  'requestsmon' : bool,
  'countrcpt' : bool, 
  'ipprobation' : float,
  'subjectprobation' : float,
  'countsentprobation' : float,
  'blockprobation' : float,
  'priority' : int,
  'jailspec' : list,
  'onlyheaders' : bool,
  'spf' : bool,
  'actionheaders' : dict
}

DEFAULT_FEATURES_VALUES = {
  'global_namespace' : 'AI',
  'global_ttl' : 86400,
  'policiesByServerPoolFeature' : True,
  'featuresByServerPool' : False,
  'messagesBySecFeature' : True,
  'messagesBySecStoreDays' : 1,
  'feederFeaturesEnabled' : False,
  'fallbackToNonPoolPolicies' : False,
  'learnFeature' : False,
  'learnPredictSafeValue' : 30.0,
  'learnOnlyOnce' : True,
  'learnEscalationValue' : 0.2,
  'learnTimeFrameValue' : [['1', '1']],
  'learnBlockMinutes' : 2,
  'spfStrictRejectFeature' : False,
  'rateReputationFeature' : False,
  'rateReputationBlockHitValue' : 5,
  'rateReputationDecreaseValue' : 0.20,
  'rateReputationIncreaseMinutes' : 0,
  'ipReputationFeature' : False,
  'ipReputationHitValue' : 4,
  'ipReputationDecreaseValue' : 0.20,
  'ipReputationIncreaseMinutes' : 0,
  'subjectReputationFeature' : False,
  'subjectReputationHitValue' : 10,
  'subjectReputationDecreaseValue' : 0.10,
  'subjectReputationIncreaseMinutes' : 0,
  'global_conditions' : [ [720, 500] ],
  'global_custom_block' : 0
}

DEFAULT_POLICY_PARAMS = {
  'Enable' : True,
  'Type' : 'regular',
  'Priority' : 5,
  'JailBy' : 'Sender+',
  'JailSpec' : '0:0',
  'JailAction' : 'monitor',
  'ReplyData' : 'Limit reached. Blocking for %s second(s)',
  'CountSentProbation' : 1,
  'CountRCPT' : False,
  'StopHere' : False,
  'RequestsMon' : False,
  'SubjectProbation' : 0.5,
  'IpProbation' : 0.5,
  'BlockProbation' : 0.5,
  'CountSentProbation' : 1,
  'ActionHeaders' : {},
  'OnlyHeaders' : False,
  'SPF' : False
}

RESERVERD_KEYWORDS = ['global', 'any', 'list', 'all', 'metadata', 'pool', 'policy', 'policies', 'group']