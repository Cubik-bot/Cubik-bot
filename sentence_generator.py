import random

nouns = ('people', 'history', 'way', 'art', 'world', 'information', 'map',
         'family', 'government', 'health', 'system', 'computer', 'meat', 'year',
         'thanks', 'music', 'person', 'reading', 'method', 'data', 'food',
         'understanding', 'theory', 'law', 'bird', 'literature', 'problem',
         'software', 'control', 'knowledge', 'power', 'ability', 'economics',
         'love', 'internet', 'television', 'science', 'library', 'nature',
         'fact', 'product', 'idea', 'temperature', 'investment', 'area',
         'society', 'activity', 'story', 'industry', 'media', 'thing',
         'oven', 'community', 'definition', 'safety', 'quality', 'development',
         'language', 'management', 'player', 'variety', 'video', 'week',
         'security', 'country', 'exam', 'movie', 'organization', 'equipment',
         'physics', 'analysis', 'policy', 'series', 'thought', 'basis',
         'boyfriend', 'direction', 'strategy', 'technology', 'army',
         'camera', 'freedom', 'paper', 'environment', 'child', 'instance',
         'month', 'truth', 'marketing', 'university', 'writing', 'article',
         'department', 'difference', 'goal', 'news', 'audience', 'fishing',
         'growth', 'income', 'marriage')

verbs = ('is', 'are', 'has', 'get', 'see', 'need', 'know', 'would', 'find', 'take',
         'want', 'does', 'learn', 'become', 'come', 'include', 'thank', 'provide',
         'create', 'add', 'understand', 'consider', 'choose', 'develop', 'remember',
         'determine', 'grow', 'allow', 'supply', 'bring', 'improve', 'maintain',
         'begin', 'exist', 'tend', 'enjoy', 'perform', 'decide', 'identify',
         'continue', 'protect', 'require', 'occur', 'write', 'approach', 'avoid',
         'prepare', 'build', 'achieve', 'believe', 'receive', 'seem', 'discuss',
         'realize', 'contain', 'follow', 'refer', 'solve', 'describe', 'prefer',
         'prevent', 'discover', 'ensure', 'expect', 'invest', 'reduce', 'speak',
         'appear', 'explain', 'explore', 'involve', 'lose', 'afford', 'agree',
         'hear', 'remain', 'represent', 'apply', 'forget', 'recommend', 'rely',
         'vary', 'generate', 'obtain', 'accept', 'communicate', 'complain',
         'depend', 'enter', 'happen', 'indicate', 'suggest', 'survive', 'appreciate',
         'compare', 'imagine', 'manage', 'differ', 'encourage', 'expand', 'prove', 'react')

adj = ('different', 'used', 'important', 'every', 'large', 'available', 'popular', 'able',
       'basic', 'known', 'various', 'difficult', 'several', 'united', 'historical', 'hot',
       'useful', 'mental', 'scared', 'additional', 'emotional', 'old', 'political',
       'similar', 'healthy', 'financial', 'medical', 'traditional', 'federal', 'entire',
       'strong', 'actual', 'significant', 'successful', 'electrical', 'expensive',
       'pregnant', 'intelligent', 'interesting', 'poor', 'happy', 'responsible', 'cute',
       'helpful', 'recent', 'willing', 'nice', 'wonderful', 'impossible', 'serious',
       'huge', 'rare', 'technical', 'typical', 'competitive', 'critical', 'electronic',
       'immediate', 'aware', 'educational', 'environmental', 'global', 'legal',
       'relevant', 'accurate', 'capable', 'dangerous', 'dramatic', 'efficient',
       'powerful', 'foreign', 'hungry', 'practical', 'psychological', 'severe',
       'suitable', 'numerous', 'sufficient', 'unusual', 'consistent', 'cultural',
       'existing', 'famous', 'pure', 'afraid', 'obvious', 'careful', 'latter', 'unhappy',
       'acceptable', 'aggressive', 'boring', 'distinct', 'eastern', 'logical', 'reasonable',
       'strict', 'administrative', 'automatic', 'civil', 'former')

adv = ('not', 'also', 'very', 'often', 'however', 'too', 'usually', 'really', 'early',
       'never', 'always', 'sometimes', 'together', 'likely', 'simply', 'generally',
       'instead', 'actually', 'again', 'rather', 'almost', 'especially', 'ever',
       'quickly', 'probably', 'already', 'below', 'directly', 'therefore', 'else',
       'thus', 'easily', 'eventually', 'exactly', 'certainly', 'normally', 'currently',
       'extremely', 'finally', 'constantly', 'properly', 'soon', 'specifically', 'ahead',
       'daily', 'highly', 'immediately', 'relatively', 'slowly', 'fairly', 'primarily',
       'completely', 'ultimately', 'widely', 'recently', 'seriously', 'frequently',
       'fully', 'mostly', 'naturally', 'nearly', 'occasionally', 'carefully', 'clearly',
       'essentially', 'possibly', 'slightly', 'somewhat', 'equally', 'greatly',
       'necessarily', 'personally', 'rarely', 'regularly', 'similarly', 'basically',
       'closely', 'effectively', 'initially', 'literally', 'mainly', 'merely', 'gently',
       'hopefully', 'originally', 'roughly', 'significantly', 'totally', 'twice',
       'elsewhere', 'everywhere', 'obviously', 'perfectly', 'physically', 'successfully',
       'suddenly', 'truly', 'virtually', 'altogether', 'anyway', 'automatically')

preps = ('of', 'with', 'at', 'from', 'into', 'during', 'until', 'to', 'in', 'for', 'on',
         'by', 'about', 'like', 'through', 'but', 'up', 'out', 'after', 'under')


def generate_sentence():
    str = random.choice(nouns) + ' '
    str += random.choice(adv) + ' '
    str += random.choice(verbs) + ' '
    str += random.choice(preps) + ' '
    str += random.choice(adj) + ' '
    str += random.choice(nouns) + ' '
    str += random.choice(adv) + ' to '
    str += random.choice(verbs) + ' '
    str += random.choice(preps) + ' '
    str += random.choice(nouns) + ' '
    str += random.choice(adj) + '.'
    char = str[0:1].upper()
    return char + str[1:]
