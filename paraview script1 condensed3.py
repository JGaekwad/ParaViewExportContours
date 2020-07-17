# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#'SE','S','SW','W','NW'

directionList=['N','NE','E']
#define screenshot z levels
levels=[1.5,6.0,11.5]
#i=100

for j in directionList:
    #Refresh session and clear data
    direction='TWEED'+str(j)
    Disconnect()
    Connect()    
    LoadState('/home/openfoam/run/TWEEDSTATE2.pvsm', LoadStateDataFileOptions='Choose File Names',
    DataDirectory='/home/openfoam/run',
    TWEEDNOpenFOAMFileName='/home/openfoam/run/TWEED'+str(j)+'/TWEED'+str(j)+'.OpenFOAM')
    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # find source
    slice1 = FindSource('Slice1')
    # set active source
    SetActiveSource(slice1)
    #select the main results so axis doesn't show on screenshot
    # find source
    tWEEDNOpenFOAM = FindSource(str(direction)+'.OpenFOAM')
    # set active source
    SetActiveSource(tWEEDNOpenFOAM)
    for i in levels:
        print (i)
        # Properties modified on slice1.SliceType
        slice1.SliceType.Origin = [170.0, 75.0, i]
        # get animation scene
        #animationScene1 = GetAnimationScene()
        #animationScene1.GoToLast()
        # save screenshot
        SaveScreenshot('/home/openfoam/run/2020.07.03 Outputs/'+str(j)+str(i) +'.png', renderView1, ImageResolution=[1612, 808])
    print(str(j)+' screens done')

print('All done')



#so the below works..?

j='W'

Disconnect()
Connect()

# load state
LoadState('/home/openfoam/run/TWEEDSTATE2.pvsm', LoadStateDataFileOptions='Choose File Names',
    DataDirectory='/home/openfoam/run',
    TWEEDNOpenFOAMFileName='/home/openfoam/run/TWEED'+str(j)+'/TWEED'+str(j)+'.OpenFOAM')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# find source
slice1 = FindSource('Slice1')
# set active source
SetActiveSource(slice1)

#select the main results so axis doesn't show on screenshot
# find source
tWEEDNOpenFOAM = FindSource('TWEEDSE.OpenFOAM') #this might be the thing
# set active source
SetActiveSource(tWEEDNOpenFOAM)

#define screenshot z levels
levels=[1.5,6.0,11.5]


#j='SE' #comment this out or delete if you're not using indiviudally
for i in levels:
    print (i)
    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [170.0, 75.0, i]
    # get animation scene
    #animationScene1 = GetAnimationScene()
    #animationScene1.GoToLast()
    # save screenshot
    SaveScreenshot('/home/openfoam/run/2020.07.03 Outputs/'+str(j)+str(i) +'.png', renderView1, ImageResolution=[1612, 808])

#it's this last line that kills it - not sure how to exit out of the loop

print(i)




#I'm not using anything below this

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [170.0, 75.0, 6.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [170.0, 75.0, 6.0]

# find source
tWEEDNOpenFOAM = FindSource('TWEEDN.OpenFOAM')

# show data in view
tWEEDNOpenFOAMDisplay = Show(tWEEDNOpenFOAM, renderView1)

# trace defaults for the display properties.
tWEEDNOpenFOAMDisplay.Representation = 'Surface'
tWEEDNOpenFOAMDisplay.ColorArrayName = [None, '']
tWEEDNOpenFOAMDisplay.OSPRayScaleArray = 'U'
tWEEDNOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
tWEEDNOpenFOAMDisplay.SelectOrientationVectors = 'None'
tWEEDNOpenFOAMDisplay.ScaleFactor = 110.0
tWEEDNOpenFOAMDisplay.SelectScaleArray = 'None'
tWEEDNOpenFOAMDisplay.GlyphType = 'Arrow'
tWEEDNOpenFOAMDisplay.GlyphTableIndexArray = 'None'
tWEEDNOpenFOAMDisplay.GaussianRadius = 5.5
tWEEDNOpenFOAMDisplay.SetScaleArray = ['POINTS', 'U']
tWEEDNOpenFOAMDisplay.ScaleTransferFunction = 'PiecewiseFunction'
tWEEDNOpenFOAMDisplay.OpacityArray = ['POINTS', 'U']
tWEEDNOpenFOAMDisplay.OpacityTransferFunction = 'PiecewiseFunction'
tWEEDNOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
tWEEDNOpenFOAMDisplay.SelectionCellLabelFontFile = ''
tWEEDNOpenFOAMDisplay.SelectionPointLabelFontFile = ''
tWEEDNOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tWEEDNOpenFOAMDisplay.DataAxesGrid.XTitleFontFile = ''
tWEEDNOpenFOAMDisplay.DataAxesGrid.YTitleFontFile = ''
tWEEDNOpenFOAMDisplay.DataAxesGrid.ZTitleFontFile = ''
tWEEDNOpenFOAMDisplay.DataAxesGrid.XLabelFontFile = ''
tWEEDNOpenFOAMDisplay.DataAxesGrid.YLabelFontFile = ''
tWEEDNOpenFOAMDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tWEEDNOpenFOAMDisplay.PolarAxes.PolarAxisTitleFontFile = ''
tWEEDNOpenFOAMDisplay.PolarAxes.PolarAxisLabelFontFile = ''
tWEEDNOpenFOAMDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
tWEEDNOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set scalar coloring
ColorBy(tWEEDNOpenFOAMDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
tWEEDNOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(tWEEDNOpenFOAM, renderView1)

animationScene1.GoToLast()

# current camera placement for renderView1
renderView1.CameraPosition = [123.78523992060661, 124.391710115953, 485.58206463951825]
renderView1.CameraFocalPoint = [123.78523992060661, 124.391710115953, 76.98927506379744]
renderView1.CameraParallelScale = 711.4438542672451

# save screenshot
SaveScreenshot('/home/openfoam/run/2020.07.03 Outputs/N 6.png', renderView1, ImageResolution=[1612, 808])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [123.78523992060661, 124.391710115953, 485.58206463951825]
renderView1.CameraFocalPoint = [123.78523992060661, 124.391710115953, 76.98927506379744]
renderView1.CameraParallelScale = 711.4438542672451

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
