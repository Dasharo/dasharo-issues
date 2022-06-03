---
name: Report Hardware Compatibility List
about: 'Report information about compatible hardware that you are using in your setup'
title: ''
labels: 'P: default, T: hcl'
assignees: ''

---

**Dasharo version**
<!--(The version of Dasharo you're using (e.g., `v0.2.0`))-->

**CPU**

* Processor name: <!--(full name including vendor, brand and CPU number))-->
* Core name: <!--(CPU core codename))-->
* CPU base speed: <!--(based CPU speed))-->
* CPU boost spped - <!--(boosted CPU speed))-->
* Wattage: <!--(declared by producer processor wattage))-->
* GPU: <!--(information about embedded graphics processing unit))-->
* Results: <!--(link to measurement results))-->

**GPU**

* GPU name: <!--(full name of GPU including vendor and chipset name))-->
* Memory size: <!--(total amount of GPU memory declared by vendor))-->
* Memory type: <!--(GPU's type of memory))-->
* Bandwith: <!--(GPU's bandwith))-->
* PCI-E Architecture: <!--(declared by producer generation of PCI-E architecture))-->
* Multi-Graphics Technology: <!--(information about support for this technology))-->

**Memory**

* Configuration 1/2/4:
<!--(means given memory module was tested in 1, 2 and 4 DIMMs populated configuration))-->
<!--(set ✔ if successfully tested, ✖ if platform did not boot with Dasharo))-->
<!--(e.g. ✔/✔/✔ means all configurations work, - means not tested))-->
* Size: <!--(DIMM capacity in GB))-->
* SPD profile: <!--(can be one of JEDEC(Standard) / XMP Profile #1 / XMP Profile #2))-->
* Profile data:
  * Type/speed:
  <!--(e.g. DDR4-2400 means DDR4 module clocked at max 2400MHz for given profile))-->
  * Timings:
  <!--(e.g CL17-17-17 means CAS Latency 17, tRCD 17, tRP 17 (numbers expressed in clock cycles) for given memory profile))-->
  * Voltage:
  <!--(memory voltage in Volts for given memory profile))-->
