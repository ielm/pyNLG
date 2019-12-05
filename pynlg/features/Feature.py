class Feature:
    def __init__(self):
        pass

    # This feature determines if the adjectives should be reordered. Some
    # lexicons might support the positioning of adjectives and by default, this
    # order will be used. The user can override the ordering of adjectives by
    # setting this feature to false.
    ADJECTIVE_ORDERING = "adjective_ordering"

    # This feature determines if the auxiliary verbs in a clause should be
    # aggregated.
    AGGREGATE_AUXILIARY = "aggregate_auxiliary";

    # The complementiser is the word that joins a subordinate clause to the
    # parent clause. For example, the two clauses: <em>Timmy sang a song</em>
    # and <em>moved Elizabeth to tears</em> can be joined with the
    # complementiser <em>that</em> to form:
    # <em>Timmy sang a song <b>that</b> moved Elizabeth to
    # tears</em>.
    COMPLEMENTISER = "complementiser"

    # This feature represents the word (or phrase) used for linking coordinated
    # phrases together.
    CONJUNCTION = "conjunction"

    # This feature represents the type of conjunction this coordination
    # represents.
    CONJUNCTION_TYPE = "conjunction_type"

    # An appositive is a type of postmodifying phrase which is quasi-synonymous
    # with, or a possible replacement of, the phrase it modifies. A typical
    # example occurs with NPs, e.g.:
    # <em>his house, <b>a large villa</b>, is on the hill</em> where the phrase
    # <em>a large villa</em> is an appositive postmodifier of
    # <em>his house</em>. Note that appositives are usually realised surrounded
    # by commas. Accordingly, this feature is primarily used by the orthography
    # processor to determine whether commas should be placed around a
    # postmodifying phrase.
    APPOSITIVE = "appositive";

    # This feature represents the cue phrase of a sentence. Cue phrases
    # sometimes appear at the start of sentences. In the following example,
    # <em>however</em> forms the cue phrase:<br>
    # <em><b>However</b>, John
    # played football instead.</em>
    CUE_PHRASE = "cue_phrase";

    # This features determines if the phrase is elided. Elided phrases are
    # omitted from the final realisation.
    ELIDED = "elided";

    # This feature dictates the form that a verb takes.
    FORM = "form";

    # This feature determines the type of interrogative (question) used for the
    # clause.
    INTERROGATIVE_TYPE = "interrogative_type";

    # This flag determines if the Adjective or Adverb should be inflected into
    # the comparative form. For example, the comparative form for
    # <em>early</em> is <em>earlier</em>, the comparative form of <em>big</em>
    # is <em>bigger</em>.
    IS_COMPARATIVE = "is_comparative";

    # This flag determines if the Adjective or Adverb should be inflected into
    # the superlative form. For example, the comparative form for
    # <em>early</em> is <em>earliest</em>, the superlative form of <em>big</em>
    # is <em>biggest</em>.
    IS_SUPERLATIVE = "is_superlative";

    # The modal represents the modal auxiliary verb that is used in a verb
    # phrase to express mood or tense. The English modals are: <em>can</em>,
    # <em>may</em>, <em>must</em>, <em>ought</em>, <em>shall</em>,
    # <em>should</em>, <em>will</em> and <em>would</em>.
    MODAL = "modal";

    # The flag determines if the corresponding verb phrase should be negated.
    # For example, negating the clause <em>John kissed Mary</em> results in the
    # clause <em>John did not kiss Mary</em>.
    NEGATED = "negated";

    # This feature is used to determine if the element is to be represented in
    # singular or plural form.
    NUMBER = "number";

    # This feature represents the pattern that a particular word follows when 
    # being inflected. These can be regular, irregular, regular double and in 
    # the case of nouns, Greco-Latin regular.
    PATTERN = "pattern";

    # This feature represents a particle used in conjunction with a verb. For
    # example, the verb phrases <em>fall down</em> and <em>look up</em> have
    # particles of <em>down</em> and <em>up</em> respectively.
    PARTICLE = "particle";

    # This flag shows if the phrase or clause should be written in the passive
    # form. For example, the clause <em>the cat ate the mouse</em> can be
    # written in the passive form as <em>the mouse was eaten by the cat</em>.
    PASSIVE = "passive";

    # This flag shows if the phrase or clause should be written in the perfect
    # form. The perfect aspect is normally formed from the auxiliary verb
    # <em>to have</em> followed by the past participle of the main verb. For
    # example, the phrase <em>the cat eats the mouse</em> would have the
    # present perfect form of <em>the cat has eaten the mouse</em>.
    PERFECT = "perfect";

    # This feature represents the first-person, second-person or third-person
    # nature of the phrase. This predominantly affects pronouns such as
    # <em>I</em>, <em>you</em> and <em>they</em> but some verbs will also be
    # modified depending on the person of reference. For example, kiss is used
    # as the present tense for first and second person (<em>I kiss Mary</em>
    # and <em>you kiss Mary</em>) while kisses is used for third person (
    # <em>he kisses Mary</em>).
    PERSON = "person";

    # This flag shows if the noun phrase should be written in the possessive
    # form. The possessive form of a noun is usually formed from the noun with
    # 's added to the end. For example, dog has a possessive form dog's. 
    # Certain personal pronouns follow different rules, the possessive form
    # of <em>I</em> is <em>mine</em>, <em>you</em> is <em>yours</em>.
    POSSESSIVE = "possessive";

    # This flag can be set for noun phrases where it is desirable to overwrite
    # the subject with a suitable pronoun.
    PRONOMINAL = "pronominal";

    # This flag determines if the verb phrase should be constructed in the
    # progressive form. For example, the progressive form of <em>John kisses
    # Mary</em> is <em>John is kissing Mary</em>.
    PROGRESSIVE = "progressive";

    # This flag can be set when specifiers in a coordinated phrase should be
    # raised. For example, the coordinated phrase <em>my cat and my dog</em>
    # can have its specifiers raised becoming <em>my cat and dog</em>.
    RAISE_SPECIFIER = "raise_specifier";

    # This flag is set when it is necessary to suppress the genitive when
    # dealing with gerund forms.
    SUPPRESS_GENITIVE_IN_GERUND = "suppress_genitive_in_gerund";

    # This flag determines if complementisers in subordinating clauses should
    # be suppressed.
    SUPRESSED_COMPLEMENTISER = "suppressed_complementiser";

    # This flag represents the tense or temporal quality of a verb.
    TENSE = "tense";
