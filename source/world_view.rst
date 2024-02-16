Location/item properties
========================

The Location/item properties view opens in the right pane when you
select a location or an item in the tree.


Title and description
---------------------

.. figure:: _images/worldView01.png
   :alt: Screenshot

Title and description are displayed in an editable "index card".

The editing of the title can be completed by pressing the ``Enter`` key.
Changes to the description are applied when the mouse is clicked
anywhere outside the text input field.

AKA
---

This entry field is for alias names. Editing can be completed
by pressing the ``Enter`` key.

Tags
----

Tags are a very freely usable tool for labeling locations and items
in the tree view. Tags do not have to be defined elsewhere, but
simply entered in the input field separated by semicolons.
Editing can be completed by pressing the ``Enter`` key.

.. caution::
   If you want to use a tag more than once, make sure you use 
   the same spelling in the different places. 

Links
-----

Expand or collapse this frame by clicking on the label.

.. figure:: _images/characterView04.png
   :alt: Screenshot
   
This is a list for image and research data links.

Although *noveltree* holds some character/location/item data, it is
not the right application for extensive world building. For this,
you may want to use more powerful software, like `Zim Desktop Wiki
<https://zim-wiki.org/>`__. In this case, *noveltree* allows you to
create links to the text files that will take you quickly to the right
places in the wiki.

Or you have collected some images that could inspire you when writing.
Then simply create links to these images to open them with your
system's standard image viewer.

.. tip::
   If you have collected several images for a character in a folder 
   that your standard image viewer can browse through, a single link 
   to any image file is sufficient.  
   
The links are displayed in a list in the order they are entered.

Add Link
   When clicking on |Add|, a file selection dialog opens. The selected
   file will be added to the link list.

   .. hint::
      By default, the dialog shows image files. For other file types, 
      change the selector in the lower right corner. 
      
      .. figure:: _images/filePicker01.png
         :alt: Screenshot
         
         Windows 10 Explorer screenshot


Remove Link
   When clicking on |Remove|, the selected link is removed from the list.

Open Link
   When double-clicking on a link, or clicking on |Goto|,
   the link is opened with the standard application for the link's file type.

   .. hint::
      If you want to open certain linked files with another application than the 
      standard application, you can provide a *noveltree* "launcher" setting. 
      For this, just create a text file named **launchers.ini** in the 
      ``.noveltree.config``  directory (where all configuration files are stored). 
      
      This example shows a setting that makes *noveltree* open text files
      with the *Zim Desktop Wiki* application instead of the standard text 
      editor: 
      
      ::
     
         [SETTINGS]
         .txt = C:/Program Files (x86)/Zim Desktop Wiki/zim.exe 
         
      .. figure:: _images/launchers.png
         :alt: Screenshot
         
         Windows 10 Explorer screenshot

.. |Add| image:: _images/add.png
.. |Goto| image:: _images/goto.png
.. |Remove| image:: _images/remove.png



Navigation buttons
------------------

Location view
~~~~~~~~~~~~~

- **Previous** moves the selection to the previous location in the tree.
- **Next** moves the selection to the next location in the tree.

Item view
~~~~~~~~~

- **Previous** moves the selection to the previous item in the tree.
- **Next** moves the selection to the next item in the tree.
