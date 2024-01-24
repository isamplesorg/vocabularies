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

[]{#iSamplesMaterialsVocabulary}

# **Concept scheme:** iSamples Materials Vocabulary 

Vocabulary last modified:  2022-03-11

subtitle: 
  High level vocabulary to specify the kind of material that constitutes a physical sample

Namespace: 
[`https://w3id.org/isample/vocabulary/material/1.0/materialsvocabulary`](https://w3id.org/isample/vocabulary/material/1.0/materialsvocabulary)

**History**

* 2022-01-05 SMR version 0.9, change base uri to https://w3id.org/isample/vocabulary/material/0.9/ for testing with ESIP COR and w3id uri resolution
* 2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes to some definitions.  Add skos matches to URIs from other vocabularies; 2023-11-05 version 1.0, in preparation for release. 

- [Material ](#material)
    - [Any anthropogenic material](#anyanthropogenicmaterial)
        - [Anthropogenic metal material ](#anthropogenicmetal)
        - [Anthropogenic material](#otheranthropogenicmaterial)
    - [Any ice](#anyice)
        - [Frozen water](#waterice)
    - [Biogenic non-organic material](#biogenicnonorganicmaterial)
    - [Dispersed media](#dispersedmedia)
    - [Natural Solid Material](#earthmaterial)
        - [Mineral ](#mineral)
        - [Mixed soil sediment or rock](#mixedsoilsedimentrock)
        - [Particulate](#particulate)
        - [Rock or sediment](#rockorsediment)
            - [Rock](#rock)
            - [Sediment](#sediment)
        - [Soil](#soil)
    - [Fluid material](#fluid)
        - [Gaseous material](#gas)
        - [Liquid water](#liquidwater)
        - [Non-aqueous liquid material ](#nonaqueousliquid)
    - [Organic material](#organicmaterial)

**Concepts**

[]{#material}

##  Material


- Top Concept in iSamples Material Category scheme
- Concept URI token: material


[]{#anyanthropogenicmaterial}

###  Any anthropogenic material


- Child of:
 [`material`](#material)

- Material produced by human activity.
- Concept URI token: anyanthropogenicmaterial


[]{#anthropogenicmetal}

####  Anthropogenic metal material


- Child of:
 [`anyanthropogenicmaterial`](#anyanthropogenicmaterial)

- Specimen is dominantly composed of metal that has been produced or
used by humans; subclass of anthropogenic material. Samples of
naturally occuring metallic material (e.g. native copper, gold
nuggets) should be considered mineral material. Metallic material is
material that when polished or fractured, shows a lustrous appearance,
and conducts electricity and heat relatively well. Metals are
typically malleable (they can be hammered into thin sheets) or ductile
(can be drawn into wires). The boundaries between metals, nonmetals,
and metalloids fluctuate slightly due to a lack of universally
accepted definitions of the categories involved.
(https://en.wikipedia.org/wiki/Metal). c.f.
http://purl.obolibrary.org/obo/ENVO_01001069
- Concept URI token: anthropogenicmetal


[]{#otheranthropogenicmaterial}

####  Anthropogenic material


- Child of:
 [`anyanthropogenicmaterial`](#anyanthropogenicmaterial)

- Non-metallic material produced by human activity. Organic products
of agricultural activity are both anthropogenic and organic. Include
lab preparations like XRF pellet and rock powders. Examples: ceramics,
concrete, slag, (anthropogenic) glass, mine tailing, plaster, waste.
- Concept URI token: otheranthropogenicmaterial


[]{#anyice}

###  Any ice


- Child of:
 [`material`](#material)

- a solid material that is normally a liquid or gas at Standard
Temperature and Pressre (STP) that is in a solid state under the
observed temperature and pressure conditions.
- Concept URI token: anyice


[]{#waterice}

####  Frozen water


- Child of:
 [`anyice`](#anyice)

- Water that is in a solid state.

- **Alternate labels:**
Water ice

- Concept URI token: waterice


[]{#biogenicnonorganicmaterial}

###  Biogenic non-organic material


- Child of:
 [`material`](#material)

- Material produced by an organism but not composed of 'very large
molecules of biological origin.' E.g. bone, tooth, shell, coral
skeleton,
- Concept URI token: biogenicnonorganicmaterial


[]{#dispersedmedia}

###  Dispersed media


- Child of:
 [`material`](#material)

- A material contains discrete elements of one medium that are
dispersed in a continuous fluid medium.  The dispersed component can
be a gas, a liquid or a solid (based on
https://en.wikipedia.org/wiki/Dispersed_media). Does not include
mixtures of granular material like soil, sediment, particulate, or
solids that would be considered a rock.
- Concept URI token: dispersedmedia


[]{#earthmaterial}

###  Natural Solid Material


- Child of:
 [`material`](#material)

- Undifferentiated soil, sediment, rock, or natural particulates.
Typically (nessarily?) a granular aggregate that might include any of
the previous constiturents. Use for Earth Material aggregates of
uncertain origin
- Concept URI token: earthmaterial


[]{#mineral}

####  Mineral


- Child of:
 [`earthmaterial`](#earthmaterial)

- Material consists of a single mineral or mineraloid phase. .  'A
mineral is an element or chemical compound that is normally
crystalline and that has been formed as a result of geological
processes.' (Nickel, Ernest H. (1995), The definition of a mineral,
The Canadian Mineralogist. 33 (3): 689–90). Include mineraloids. ... A
material primarily composed of some substance that is naturally
occurring, solid and stable at room temperature, representable by a
chemical formula, usually abiogenic, and that has an ordered atomic
structure. (http://purl.obolibrary.org/obo/ENVO_01000256). Comment:
the identity of a mineral species is defined by a crystal structure
and a chemical composition that might include various specific
elemental substitutions in that structure. Mineraloid: A naturally
occurring mineral-like substance that does not demonstrate
crystallinity. Mineraloids possess chemical compositions that vary
beyond the generally accepted ranges for specific minerals. Examples:
obsidian, Opal. (https://en.wikipedia.org/wiki/Mineraloid)
- Concept URI token: mineral


[]{#mixedsoilsedimentrock}

####  Mixed soil sediment or rock


- Child of:
 [`earthmaterial`](#earthmaterial)

- Material is mixed aggregation of fragments of undifferentiated soil,
sediment or rock origin. e.g. cuttings from some boreholes (rock
fragments and caved soil or sediment).
- Concept URI token: mixedsoilsedimentrock


[]{#particulate}

####  Particulate


- Child of:
 [`earthmaterial`](#earthmaterial)

- Material consists of microscopic particulate material derived by
precipitation, filtering, or settling from suspension in a fluid, e.g.
filtrate from water, deposition from atmosphere, astro material
particles. Might include mineral, organic, or biological material.
ENVO definition (ENVO_01000060) has "composed of microscopic portions
of solid or liquid material suspended in another environmental
material.", refine here to define as the solid particles, distinct
from a material in which they are suspended. A material that includes
solid or liquid particles suspended in another material would be a
dispersed_media in this scheme, not defined in ENVO. Human
manufactured particulates (e.g. rock powder) should be categorized as
'anthropogenic material' as well as 'Particulate'
- Concept URI token: particulate


[]{#rockorsediment}

####  Rock or sediment


- Child of:
 [`earthmaterial`](#earthmaterial)

- Material is rock or sediment.  E.g. for samples from subsurface
cores that are not well described, from drill holes that likely
penetrate sediment near the surface an might be sampling rock at
greater depth.
- Concept URI token: rockorsediment


[]{#rock}

#####  Rock


- Child of:
 [`rockorsediment`](#rockorsediment)

- Consolidated aggregate of particles (grains) of rock, mineral
(including native elements), mineraloid, or solid organic material.
Includes mineral aggregates such as granite, shale, marble; natural
glass such as obsidian; organic material formed by geologic processes
such a coal;  extraterrestrial material in meteorites; and  crushed
rock fragments like drill cuttings from rock.  (based on
http://resource.geosciml.org/classifier/cgi/lithology/rock, same as
http://purl.obolibrary.org/obo/ENVO_00001995)

- See Also:
* [<http://purl.obolibrary.org/obo/ENVO_00001995>](http://purl.obolibrary.org/obo/ENVO_00001995)
* [<http://resource.geosciml.org/classifier/cgi/lithology/rock>](http://resource.geosciml.org/classifier/cgi/lithology/rock)
- Concept URI token: rock


[]{#sediment}

#####  Sediment


- Child of:
 [`rockorsediment`](#rockorsediment)

- Solid granular material transported by wind, water, or gravity, not
modified by interaction with biosphere or atmosphere (to differentiate
from soil). Particles derived by erosion of pre-existing rock, from
shell or other body parts from organisms, precipitated chemically in
the surficial environment, or generated by explosive volcanic
activity.
(http://resource.geosciml.org/classifier/cgi/lithology/sediment).
Sediment is not consolidated, i.e. Particulate constituents of a
compound material do not adhere to each other strongly enough that the
aggregate can be considered a solid material in its own right. Similar
to http://purl.obolibrary.org/obo/ENVO_00002007
- Concept URI token: sediment


[]{#soil}

####  Soil


- Child of:
 [`earthmaterial`](#earthmaterial)

- Mixed granular mineral and organic matter modified by interaction
between earth material, biosphere, and atmosphere, consisting mostly
of varying proportions of sand, silt, and clay, organic material such
as humus, gases, liquids, and a broad range of resident micro- and
macroorganisms. (https://en.wikipedia.org/wiki/Soil) Soil consists of
horizons near the Earth's surface that, in contrast to the underlying
parent material, have been altered by the interactions of climate,
relief, and living organisms over time. (http://www.nrcs.usda.gov/wps/
portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
(http://purl.obolibrary.org/obo/ENVO_00001998)

- See Also:
* [<http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280>](http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
- Concept URI token: soil


[]{#fluid}

###  Fluid material


- Child of:
 [`material`](#material)

- a substance that continually deforms (flows) under an applied shear
stress, or external force. Fluids are a phase of matter and include
liquids, gases and plasmas. They are substances with zero shear
modulus, or, in simpler terms, substances that cannot resist any shear
force applied to them. (https://en.wikipedia.org/wiki/Fluid)
- Concept URI token: fluid


[]{#gas}

####  Gaseous material


- Child of:
 [`fluid`](#fluid)

- Material composed of one or more chemical entities that has neither
independent shape nor volume but tends to expand indefinitely
(http://purl.obolibrary.org/obo/ENVO_01000797). Infer that the sample
is curated in some kind of container.
- Concept URI token: gas


[]{#liquidwater}

####  Liquid water


- Child of:
 [`fluid`](#fluid)

- A material primarily composed of dihydrogen oxide in its liquid
form; infer that the sample is curated in some kind of container.
- Concept URI token: liquidwater


[]{#nonaqueousliquid}

####  Non-aqueous liquid material


- Child of:
 [`fluid`](#fluid)

- Liquid composed dominantly of material other than water. Includes
liquids that do not fit in any other category. E.g. alcohol,
petroleum.
- Concept URI token: nonaqueousliquid


[]{#organicmaterial}

###  Organic material


- Child of:
 [`material`](#material)

- Environmental material derived from living organisms and composed
primarily of one or more very large molecules of biological origin.
Examples: body (animal or plant), body part, fecal matter, seeds,
wood, tissue, biological fluids, biological waste, algal material,
biofilm, necromass, plankton. source:
http://purl.obolibrary.org/obo/ENVO_01000155
- Concept URI token: organicmaterial



