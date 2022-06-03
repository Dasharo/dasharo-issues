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

* Processor name: <!--(full name including vendor, model and CPU number))-->
* Core name (optional): <!--(CPU core codename))-->
* CPU base speed (optional): <!--(based CPU speed))-->
* CPU boost speed (optional): <!--(boosted CPU speed))-->
* Wattage (optional): <!--(declared by producer processor wattage))-->
* GPU (optional): <!--(information about embedded graphics processing unit))-->

**GPU**

* GPU name: <!--(full name of GPU including vendor and chipset name))-->
* Memory size: <!--(total amount of GPU memory declared by vendor))-->
* Memory type: <!--(GPU's type of memory))-->
* Bandwith (optional): <!--(GPU's bandwith))-->
* PCI-E Architecture (optional): <!--(declared by producer generation of PCI-E architecture))-->
* Multi-Graphics Technology (optional): <!--(information about support for this technology))-->

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

**Dasharo Tools Suite logs (optional)**
<!--(Run and provide logs from the DTS tool))-->
<!--(https://github.com/Dasharo/docs/pull/212/files))-->
