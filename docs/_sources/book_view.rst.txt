Book properties
===============

.. |ico01| image:: _images/viewBook.png
   :alt: Book

The Book properties view opens in the right pane when you
select "Book" in the tree, or when you click on the |ico01|
toolbar icon. It is the initial view after opening a *noveltree* project.

.. figure:: _images/bookView01.png
   :alt: noveltree screenshot


Title, description, and author
------------------------------

Title and description are displayed in an editable "index card".

The editing of book title and author can be completed by pressing the ``Enter`` key.
Changes to the description are applied when the mouse is clicked
anywhere outside the text input field.

After exporting the book to an *.odt* document, title and description
appear in the document properties.

.. figure:: _images/bookView08.png
   :alt: Screenshot

   LibreOffice Writer screenshot

These properties are visible, for example, when the mouse pointer is over
the document in the Windows Explorer.

.. figure:: _images/bookView09.png
   :alt: Screenshot
   
   Windows 10 Explorer screenshot
   


Document language
-----------------

Expand or collapse this frame by clicking on the label.

.. figure:: _images/bookView02.png
   :alt: noveltree screenshot

- Language code acc. to ISO 639-1
- Country code acc. to ISO 3166-2

This information controls the spelling checker for export documents.

.. figure:: _images/bookView10.png
   :alt: LibreOffice Writer screenshot

   LibreOffice Writer screenshot

If not set, the System locale setting will be used as default.


.. hint::
   You can also set or change the document language with LibreOffice, then it will be applied on import. 

	.. figure:: _images/bookView11.png
	   :alt: LibreOffice Writer screenshot
	   
	   LibreOffice Writer screenshot


Auto numbering
--------------

Expand or collapse this frame by clicking on the label.

.. figure:: _images/bookView03.png
   :alt: noveltree screenshot

Auto number chapters/parts when refreshing the tree
   If this checkbox is ticked, all chapters/parts are automatically numbered
   each time `the tree is refreshed <file_menu.html#refresh-tree>`__.
   The chapter titles are replaced with a ``prefix-number-suffix``
   pattern (without the dashes).

   .. hint::   
      You can optionally exclude individual chapters/parts from auto-numbering 
      in the `Chapter/part properties <chapter_view.html#do-not-auto-number>`__.

Prefix and suffix entries can be completed by pressing the ``Enter`` key.

.. note::
   Make sure to add a space character to separate the prefix or
   suffix from the chapter or part number.

Use Roman chapter numbers
   By default, arabic numbers, like "1", "2", "3" ... are used for auto-numbering.
   If this checkbox is ticked, Roman numbers, like "I", "II", "III", "IV" ...
   are used instead.

Reset chapter numbers when starting a new part
   By default, the chapters are numbered consistently across the parts.
   If this checkbox is ticked, the chapter numbering starts again with "1"
   in each part.


Renamings
---------

Expand or collapse this frame by clicking on the label.

.. figure:: _images/bookView04.png
   :alt: noveltree screenshot



Narrative time
--------------

Expand or collapse this frame by clicking on the label.

.. figure:: _images/bookView05.png
   :alt: noveltree screenshot

Reference date
   Format: *YYYY-MM-DD*, according to ISO 8601.

Convert dates to days


Convert days to dates

Writing pogress
---------------

Expand or collapse this frame by clicking on the label.

.. figure:: _images/bookView06.png
   :alt: noveltree screenshot



Cover thumbnail
---------------

A cover thumbnail is displayed with the book properties if you
provide a PNG image file with the project name along with the *.novx*
file. The recommended image width is 100 to 200 pixels.

.. figure:: _images/bookView12.png
   :alt: Windows 10 Explorer screenshot
   
   Windows 10 Explorer screenshot
   
.. figure:: _images/bookView07.jpg
   :alt: noveltree screenshot

   noveltree screenshot

