Section properties
==================

The Section properties view opens in the right pane when you
select a section in the tree.


.. figure:: _images/sectionView01.png
   :alt: Screenshot

Title and description
---------------------

Title and description are displayed in an editable "index card".

The editing of the title can be completed by pressing the ``Enter`` key.
Changes to the description are applied when the mouse is clicked
anywhere outside the text input field.

Plot
----

Expand or collapse this frame by clicking on the label.

Action/Reaction
---------------

Expand or collapse this frame by clicking on the label.

Relationships
-------------

Expand or collapse this frame by clicking on the label.

Add Relationship
   When clicking on |Add|, the "Pick mode"
   is activated, and the cursor changes to a "plus" shape. By clicking
   on a character/location/item, this element will be related with the section.

   .. hint::
      You can exit the "Pick mode" without selecting an element by
      clicking on the highlighted status bar, or by pressing the ``Esc``
      key. 

Remove Relationship
   When clicking on |Remove|, the selected relationship is removed from the list.

View the related element
   When double-clicking on a related element, or clicking on |Goto|,
   the selected element is opened and its properties are displayed.

   .. hint::
      You can go back to the initially selected section with |Go Back|. 

.. |Add| image:: _images/add.png
.. |Goto| image:: _images/goto.png
.. |Remove| image:: _images/remove.png
.. |Go back| image:: _images/goBack.png


Date/Time
---------

Here you can enter information about the selected section's narrative time.

.. hint::
   Dedicated timeline software offers a more convenient way of entering date/time 
   and duration information. So if chronology is important to your story, you
   might want to take a look at the `Timeline plugin 
   <https://peter88213.github.io/noveltree_timeline/>`_, or the 
   `Aeon Timeline 2 plugin <https://peter88213.github.io/noveltree_aeon2/>`_.

Start
~~~~~

If the selected section is a scene, this is when it starts:

Date
   Format: *YYYY-MM-DD*, according to ISO 8601.

Time
   Format: *hh:mm*, according to ISO 8601.

Day
   Format: Any number. Day "0" is the `reference date
   <book_view.html#narrative-time>`_, if set.

.. note::
   All entries are optional. You can either enter a date, or a day. 
   
Clear date/time
   This removes Date/Time/Day data from the selected section.

Generate
   This generates date and time from the date/time/duration data of the
   `previous section <Navigation buttons_>`_, so the selected section
   follows directly the previous one.

Convert date/day
   If the `reference date <book_view.html#narrative-time>`_ is set,
   The implicit *Day* can be transformed into an explicit *Date*,
   and vice versa.

   .. hint::
      If necessary, you can convert all sections at once in the 
      `Book properties view <book_view.html#narrative-time>`_.
   

Duration
~~~~~~~~



"Sticky note"
-------------

The yellow text area is for notes. Changes are applied
when the mouse is clicked anywhere outside the text input field.

When the "sticky note" of a section contains text, an "N" is
displayed in the tree view as a reminder. If the branch of a chapter
with sections containing notes is collapsed, the "N" is displayed
in the chapter row.

.. note::
   The "sticky notes" are only for working with *noveltree*.
   They are not meant to be exported into a document.
   However, they appear in the `section list`_.

.. _section list: section_menu.html#export-section-list-spreadsheet

Navigation buttons
------------------

- **Previous** moves the selection to the previous section in the tree.
- **Next** moves the selection to the next section in the tree.
