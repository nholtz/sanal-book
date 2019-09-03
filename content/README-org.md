## File Organization:

 * all text files (markdown, html, etc) will be under the 'text' folder.
 * all notebook files will be under the 'nb' folder.
   * this hopefully makes it eaiser for students to have their own copies of the notebook (see https://syzygy.ca/).
 * under each of those is a folder for the major topic areas:
   * `fundamentals` - Fundamental concepts
   * `sdbeams` - Statically Determinate Beams and Frames
   * etc.
 * under each of those is an `images` folder containing all images for all pages in that topic area
 * under each image folder is a subfolder containing images for just one page
   * eg `nb/fundamentals/images/eq/...` are images for one notebook page on equilibrium
 * when images are include in both notebook and text pages, the notebook pages are master
   with symlinks in the text figures.
   
 **This may be a maintenance nightmare.** We will try it for a while
 
 The overiding criteria is to make to easier to manage notebook copies for students.
 
