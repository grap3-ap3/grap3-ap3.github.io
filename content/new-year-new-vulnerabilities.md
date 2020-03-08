Title: New Year, New Vulnerabilities
Date: 2018-01-05 12:19
Author: Phil Grimes
Category: Blog
Tags: Security
Slug: new-year-new-vulnerabilities
Status: published

Well, we got to ring in the new year with some major excitement, haven't we? 2018 has met us with a nasty 1-2 punch combination, no doubt! First, the exposure of a vulnerability that effects `millions of GPS tracking devices <https://www.csoonline.com/article/3245312/security/gps-tracking-vulnerabilities-leave-millions-of-products-at-risk.html>`__. Security researchers were able to access location history, send commands to the device (the same commands that would be sent via SMS), and activate or deactivate geo fencing alarms. All this was said to be possible with no authentication needed.

This was immediately followed up by the Meltdown and Spectre vulnerabilities in what is essentially anything device connected to the internet. From mobile phones, to tablets, to laptop and desktop PCs, these flaws do expose us to some pretty significant risk. But the world is not, in fact, over. Not yet at least.

The `RedLegg <https://www.redlegg.com>`__ team has been fielding calls from clients, friends, and family about these vulnerabilities that have been drawing a lot of attention this week. There is significant implication as to the damage that could result from successful exploit of these issues, but we wanted to present some additional facts for consideration. Here's what we know:

##Meltdown

This vulnerability allows any application to access all system memory, including memory allocated for the kernel. Patches are being , and in some cases have been, rolled out and should be applied as soon as possible. So far, research indicates that only Intel chips have been shown to be vulnerable.

##Spectre

This vulnerability allows an application to force another application to access arbitrary portions of its memory, which can then be read through a side channel and affects nearly every CPU built on the x86 architecture. This vulnerability may require changes to processor architecture in order to fully mitigate. According to leading research, this vulnerability impacts Intel, AMD, and ARM chips. Due to the development life-cycle implemented by processor manufacturers, this issue will likely be around for a very long time.

Exploitation is possible. Security researchers produced and release proof of concept exploit code within roughly a day. There is no reason to believe that the bad guys will be working feverishly to weaponize these and deploy them for nefarious means. And while there definitely is significant risk associated with these vulnerabilities, there is no proof or reason to believe weaponized exploit code is in use in "the wild".

Consider taking an inventory of all your systems by processor type, be sure to apply vendor patches as they become available, and track the progress of the updates as they're released.

-  Microsoft has issued a patch for Windows 10, while other versions of Windows will be patched on the traditional Patch Tuesday on January 9, 2018.
-  MacOS 10.13.2 mitigates some of the disclosed vulnerabilities, but MacOS 10.13.3 will enhance or complete these mitigations.

For anyone using Qualys Vulnerability Management, Qualys will continue to release QIDs for any vendor patches that mitigate this vulnerability. A list of currently-released QIDs is being maintained in this \ `Qualys Support article <https://qualys.secure.force.com/articles/How_To/000002746>`__.

It's an increasingly interesting time to be in the world of security, and an increasingly dangerous time to fall victim. Take the time to read the information that's out there on these issues, there is a lot. But be sure to understand what you're reading. Proof of concept exploits for these issues continue to surface, and with each release the potential for a weaponized exploit increases. Considering the number of devices impacted here, we really need to be watching the horizon as the research develops.

Happy New Year. Stay safe out there!