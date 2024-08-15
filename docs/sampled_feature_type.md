---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
format:
  html:
    ascii: true
    toc: true
    toc-depth: 4
    number-sections: true
    anchor-sections: false
    number-depth: 8
execute:
  echo: false
---

[]{#SampledFeatureTypevocabulary}

# **Concept scheme:** Sampled Feature Type vocabulary

Vocabulary last modified:  2024-04-19

subtitle: 
  Categories to specify the broad context that a sample is intended to represent.

Namespace: 
[`https://w3id.org/isample/vocabulary/sampledfeature/1.0/sampledfeaturevocabulary`](https://w3id.org/isample/vocabulary/sampledfeature/1.0/sampledfeaturevocabulary)

**History**

* 2021-07-09  Remove Marine biome, Subaerial terrestrial environment, Subaqueous terrestrial environment per github issue https://github.com/isamplesorg/metadata/issues/41. Make Experiment setting and Laboratory or curatorial environment subclasses of Active human occupation site.
* 2021-12-10 SMR add missing skos:inScheme statements
* 2022-01-07 SMR change to https://w3id.org/isample/ uri base, make the ConceptScheme an ontology as well. For uploading to ESIP COR and w3id resolution redirect set up. Add some mappings to other ontologies using seeAlso, closeMatch, narrowMatch.
* 2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes in definitions. Add skos matches to URIs from other vocabularies. Fix typo in glacierenvrionment URI (changed the URI to glacierenvironment)
* 2022-09-07 SMR update some of the skos mappings to other vocabularies; remove references to other vocabularies as NamedIndividual. Remove rocksample class, it was not linked in hierarchy and inconsistent with design.
* 2022-09-30 add biological entity as sampled feature, per issue https://github.com/isamplesorg/metadata/issues/107. This update was lost at some point and added back in 2022-12-09.
* 2023-11-05 SMR update version to 1.0, prep for release
* 2024-04-19 SMR update definitions to remove use of 'specimen'. Edit some definitions for better clarity

- [Any sampled feature](#anysampledfeature)
    - [Anthropogenic environment](#anthropogenicenvironment)
        - [Active human occupation site](#activehumanoccupationsite)
            - [Experiment setting](#experimentsetting)
            - [Laboratory or curatorial environment](#laboratorycuratorialenvironment)
        - [Site of past human activities](#pasthumanoccupationsite)
    - [Biological entity](#biologicalentity)
    - [Earth environment](#earthenvironment)
        - [Atmosphere](#atmosphere)
        - [Earth interior](#earthinterior)
        - [Earth surface](#earthsurface)
            - [Lake river or stream bottom](#lakeriverstreambottom)
            - [Marine water body bottom](#marinewaterbodybottom)
            - [Subaerial surface environment](#subaerialsurfaceenvironment)
        - [Glacier environment](#glacierenvironment)
        - [Subsurface fluid reservoir](#subsurfacefluidreservoir)
        - [Water body](#waterbody)
            - [Marine environment](#marinewaterbody)
            - [Terrestrial water body](#terrestrialwaterbody)
    - [Extraterrestrial environment](#extraterrestrialenvironment)

**Concepts**

[]{#anysampledfeature}

##  Any sampled feature


- Any thing that can be sampled. Top concept in sampled feature type
vocabulary.
- Concept URI token: anysampledfeature


[]{#anthropogenicenvironment}

###  Anthropogenic environment


- Child of:
 [`anysampledfeature`](#anysampledfeature)

- Sampled feature is produced by or related to human activity past or
present.
- Concept URI token: anthropogenicenvironment


[]{#activehumanoccupationsite}

####  Active human occupation site


- Child of:
 [`anthropogenicenvironment`](#anthropogenicenvironment)

- sampled feature is a site at which there are ongoing human
activities
- Concept URI token: activehumanoccupationsite


[]{#experimentsetting}

#####  Experiment setting


- Child of:
 [`activehumanoccupationsite`](#activehumanoccupationsite)

- Sampled feature is an experimental set up that produced the sample;
the sample is the product of the experiment.
- Concept URI token: experimentsetting


[]{#laboratorycuratorialenvironment}

#####  Laboratory or curatorial environment


- Child of:
 [`activehumanoccupationsite`](#activehumanoccupationsite)

- Sampled feature is a laboratory or other research site, collected
with intention of characterizing the environment in which data are
collected or other research conducted, that might affect results or
safety; e.g. lab blank measurements.
- Concept URI token: laboratorycuratorialenvironment


[]{#pasthumanoccupationsite}

####  Site of past human activities


- Child of:
 [`anthropogenicenvironment`](#anthropogenicenvironment)

- sampled feature is a place where humans have been and left evidence
of their activity. Includes prehistoric and paleo hominid sites
- Concept URI token: pasthumanoccupationsite


[]{#biologicalentity}

###  Biological entity


- Child of:
 [`anysampledfeature`](#anysampledfeature)

- Sampled feature is an organism. Use for samples that represent some
species of organism as the proximate sampled feature, not the
environment that the organism inhabits.
- Concept URI token: biologicalentity


[]{#earthenvironment}

###  Earth environment


- Child of:
 [`anysampledfeature`](#anysampledfeature)

- Sampled feature is the natural Earth environment

- See Also:
* [<http://purl.bioontology.org/ontology/MESH/D004777>](http://purl.bioontology.org/ontology/MESH/D004777)
* [<http://semanticscience.org/resource/SIO_000955>](http://semanticscience.org/resource/SIO_000955)
- Concept URI token: earthenvironment


[]{#atmosphere}

####  Atmosphere


- Child of:
 [`earthenvironment`](#earthenvironment)

- Sampled feature is the Earth's atmosphere

- See Also:
* [<http://purl.obolibrary.org/obo/ENVO_01000267>](http://purl.obolibrary.org/obo/ENVO_01000267)
* [<http://purl.obolibrary.org/obo/RBO_00000018>](http://purl.obolibrary.org/obo/RBO_00000018)
- Concept URI token: atmosphere


[]{#earthinterior}

####  Earth interior


- Child of:
 [`earthenvironment`](#earthenvironment)

- Sampled feature is solid material from within the Earth
- Concept URI token: earthinterior


[]{#earthsurface}

####  Earth surface


- Child of:
 [`earthenvironment`](#earthenvironment)

- Sampled feature is the interface between solid earth and hydrosphere
or atmosphere. Includes samples representing things collected on the
surface, in the uppermost part of the material below the surface, or
air or water directly at the contact with the Earth surface.
- Concept URI token: earthsurface


[]{#lakeriverstreambottom}

#####  Lake river or stream bottom


- Child of:
 [`earthsurface`](#earthsurface)

- Sampled feature is the interface between the solid Earth interface
and a lake or flowing water body.
- Concept URI token: lakeriverstreambottom


[]{#marinewaterbodybottom}

#####  Marine water body bottom


- Child of:
 [`earthsurface`](#earthsurface)

- Sampled feature is the interface between the solid Earth and a
marine or brackish water body. Includes benthic boundary layer:  the
bottom layer of water and the uppermost layer of sediment directly
influenced by the overlying water.

- **Alternate labels:**
Sea floor

- Concept URI token: marinewaterbodybottom


[]{#subaerialsurfaceenvironment}

#####  Subaerial surface environment


- Child of:
 [`earthsurface`](#earthsurface)

- sampled feature is the interface between solid Earth and atmosphere.
Sample is collected on the surface, or immediately below surface (zone
of bioturbation). Include soil and recently deposited subaerial
sediment at the surface.
- Concept URI token: subaerialsurfaceenvironment


[]{#glacierenvironment}

####  Glacier environment


- Child of:
 [`earthenvironment`](#earthenvironment)

- Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock
or water directly under or on top of such ice.
- Concept URI token: glacierenvironment


[]{#subsurfacefluidreservoir}

####  Subsurface fluid reservoir


- Child of:
 [`earthenvironment`](#earthenvironment)

- Sampled feature is fluid that resides in fractures, intergranular
porosity or other open space in the solid earth.
- Concept URI token: subsurfacefluidreservoir


[]{#waterbody}

####  Water body


- Child of:
 [`earthenvironment`](#earthenvironment)

- Sampled feature is the Earth's hydrosphere.
- Concept URI token: waterbody


[]{#marinewaterbody}

#####  Marine environment


- Child of:
 [`waterbody`](#waterbody)

- Sampled feature is the marine hydrosphere.

- See Also:
* [<http://purl.obolibrary.org/obo/ENVO_01000686>](http://purl.obolibrary.org/obo/ENVO_01000686)
- Concept URI token: marinewaterbody


[]{#terrestrialwaterbody}

#####  Terrestrial water body


- Child of:
 [`waterbody`](#waterbody)

- Sampled feature is terrestrial hydrosphere-- lake, other standing
water, or a flowing water body (river, stream..). Include saline water
in terrestrial evaporite environments.
- Concept URI token: terrestrialwaterbody


[]{#extraterrestrialenvironment}

###  Extraterrestrial environment


- Child of:
 [`anysampledfeature`](#anysampledfeature)

- Sampled feature is the environment outside of solid earth,
hydrosphere, or atmosphere.
- Concept URI token: extraterrestrialenvironment



