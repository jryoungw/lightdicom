"""
DICOM UID dictionary

Forked from

https://github.com/pydicom/pydicom/blob/0949488c8912b13e6ad6078afa93f2a86cd53538/pydicom/_uid_dict.py
"""


UID_dictionary = {
    '1.2.840.10008.1.1': ('Verification SOP Class', 'SOP Class', '', '', 'Verification'),  # noqa
    '1.2.840.10008.1.2': ('Implicit VR Little Endian', 'Transfer Syntax', 'Default Transfer Syntax for DICOM', '', 'ImplicitVRLittleEndian'),  # noqa
    '1.2.840.10008.1.2.1': ('Explicit VR Little Endian', 'Transfer Syntax', '', '', 'ExplicitVRLittleEndian'),  # noqa
    '1.2.840.10008.1.2.1.99': ('Deflated Explicit VR Little Endian', 'Transfer Syntax', '', '', 'DeflatedExplicitVRLittleEndian'),  # noqa
    '1.2.840.10008.1.2.2': ('Explicit VR Big Endian', 'Transfer Syntax', '', 'Retired', 'ExplicitVRBigEndian'),  # noqa
    '1.2.840.10008.1.2.4.50': ('JPEG Baseline (Process 1)', 'Transfer Syntax', 'Default Transfer Syntax for Lossy JPEG 8 Bit Image Compression', '', 'JPEGBaseline8Bit'),  # noqa
    '1.2.840.10008.1.2.4.51': ('JPEG Extended (Process 2 and 4)', 'Transfer Syntax', 'Default Transfer Syntax for Lossy JPEG 12 Bit Image Compression (Process 4 only)', '', 'JPEGExtended12Bit'),  # noqa
    '1.2.840.10008.1.2.4.52': ('JPEG Extended (Process 3 and 5)', 'Transfer Syntax', '', 'Retired', 'JPEGExtended35'),  # noqa
    '1.2.840.10008.1.2.4.53': ('JPEG Spectral Selection, Non-Hierarchical (Process 6 and 8)', 'Transfer Syntax', '', 'Retired', 'JPEGSpectralSelectionNonHierarchical68'),  # noqa
    '1.2.840.10008.1.2.4.54': ('JPEG Spectral Selection, Non-Hierarchical (Process 7 and 9)', 'Transfer Syntax', '', 'Retired', 'JPEGSpectralSelectionNonHierarchical79'),  # noqa
    '1.2.840.10008.1.2.4.55': ('JPEG Full Progression, Non-Hierarchical (Process 10 and 12)', 'Transfer Syntax', '', 'Retired', 'JPEGFullProgressionNonHierarchical1012'),  # noqa
    '1.2.840.10008.1.2.4.56': ('JPEG Full Progression, Non-Hierarchical (Process 11 and 13)', 'Transfer Syntax', '', 'Retired', 'JPEGFullProgressionNonHierarchical1113'),  # noqa
    '1.2.840.10008.1.2.4.57': ('JPEG Lossless, Non-Hierarchical (Process 14)', 'Transfer Syntax', '', '', 'JPEGLossless'),  # noqa
    '1.2.840.10008.1.2.4.58': ('JPEG Lossless, Non-Hierarchical (Process 15)', 'Transfer Syntax', '', 'Retired', 'JPEGLosslessNonHierarchical15'),  # noqa
    '1.2.840.10008.1.2.4.59': ('JPEG Extended, Hierarchical (Process 16 and 18)', 'Transfer Syntax', '', 'Retired', 'JPEGExtendedHierarchical1618'),  # noqa
    '1.2.840.10008.1.2.4.60': ('JPEG Extended, Hierarchical (Process 17 and 19)', 'Transfer Syntax', '', 'Retired', 'JPEGExtendedHierarchical1719'),  # noqa
    '1.2.840.10008.1.2.4.61': ('JPEG Spectral Selection, Hierarchical (Process 20 and 22)', 'Transfer Syntax', '', 'Retired', 'JPEGSpectralSelectionHierarchical2022'),  # noqa
    '1.2.840.10008.1.2.4.62': ('JPEG Spectral Selection, Hierarchical (Process 21 and 23)', 'Transfer Syntax', '', 'Retired', 'JPEGSpectralSelectionHierarchical2123'),  # noqa
    '1.2.840.10008.1.2.4.63': ('JPEG Full Progression, Hierarchical (Process 24 and 26)', 'Transfer Syntax', '', 'Retired', 'JPEGFullProgressionHierarchical2426'),  # noqa
    '1.2.840.10008.1.2.4.64': ('JPEG Full Progression, Hierarchical (Process 25 and 27)', 'Transfer Syntax', '', 'Retired', 'JPEGFullProgressionHierarchical2527'),  # noqa
    '1.2.840.10008.1.2.4.65': ('JPEG Lossless, Hierarchical (Process 28)', 'Transfer Syntax', '', 'Retired', 'JPEGLosslessHierarchical28'),  # noqa
    '1.2.840.10008.1.2.4.66': ('JPEG Lossless, Hierarchical (Process 29)', 'Transfer Syntax', '', 'Retired', 'JPEGLosslessHierarchical29'),  # noqa
    '1.2.840.10008.1.2.4.70': ('JPEG Lossless, Non-Hierarchical, First-Order Prediction (Process 14 [Selection Value 1])', 'Transfer Syntax', 'Default Transfer Syntax for Lossless JPEG Image Compression', '', 'JPEGLosslessSV1'),  # noqa
    '1.2.840.10008.1.2.4.80': ('JPEG-LS Lossless Image Compression', 'Transfer Syntax', '', '', 'JPEGLSLossless'),  # noqa
    '1.2.840.10008.1.2.4.81': ('JPEG-LS Lossy (Near-Lossless) Image Compression', 'Transfer Syntax', '', '', 'JPEGLSNearLossless'),  # noqa
    '1.2.840.10008.1.2.4.90': ('JPEG 2000 Image Compression (Lossless Only)', 'Transfer Syntax', '', '', 'JPEG2000Lossless'),  # noqa
    '1.2.840.10008.1.2.4.91': ('JPEG 2000 Image Compression', 'Transfer Syntax', '', '', 'JPEG2000'),  # noqa
    '1.2.840.10008.1.2.4.92': ('JPEG 2000 Part 2 Multi-component Image Compression (Lossless Only)', 'Transfer Syntax', '', '', 'JPEG2000MCLossless'),  # noqa
    '1.2.840.10008.1.2.4.93': ('JPEG 2000 Part 2 Multi-component Image Compression', 'Transfer Syntax', '', '', 'JPEG2000MC'),  # noqa
    '1.2.840.10008.1.2.4.94': ('JPIP Referenced', 'Transfer Syntax', '', '', 'JPIPReferenced'),  # noqa
    '1.2.840.10008.1.2.4.95': ('JPIP Referenced Deflate', 'Transfer Syntax', '', '', 'JPIPReferencedDeflate'),  # noqa
    '1.2.840.10008.1.2.4.100': ('MPEG2 Main Profile / Main Level', 'Transfer Syntax', '', '', 'MPEG2MPML'),  # noqa
    '1.2.840.10008.1.2.4.101': ('MPEG2 Main Profile / High Level', 'Transfer Syntax', '', '', 'MPEG2MPHL'),  # noqa
    '1.2.840.10008.1.2.4.102': ('MPEG-4 AVC/H.264 High Profile / Level 4.1', 'Transfer Syntax', '', '', 'MPEG4HP41'),  # noqa
    '1.2.840.10008.1.2.4.103': ('MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1', 'Transfer Syntax', '', '', 'MPEG4HP41BD'),  # noqa
    '1.2.840.10008.1.2.4.104': ('MPEG-4 AVC/H.264 High Profile / Level 4.2 For 2D Video', 'Transfer Syntax', '', '', 'MPEG4HP422D'),  # noqa
    '1.2.840.10008.1.2.4.105': ('MPEG-4 AVC/H.264 High Profile / Level 4.2 For 3D Video', 'Transfer Syntax', '', '', 'MPEG4HP423D'),  # noqa
    '1.2.840.10008.1.2.4.106': ('MPEG-4 AVC/H.264 Stereo High Profile / Level 4.2', 'Transfer Syntax', '', '', 'MPEG4HP42STEREO'),  # noqa
    '1.2.840.10008.1.2.4.107': ('HEVC/H.265 Main Profile / Level 5.1', 'Transfer Syntax', '', '', 'HEVCMP51'),  # noqa
    '1.2.840.10008.1.2.4.108': ('HEVC/H.265 Main 10 Profile / Level 5.1', 'Transfer Syntax', '', '', 'HEVCM10P51'),  # noqa
    '1.2.840.10008.1.2.5': ('RLE Lossless', 'Transfer Syntax', '', '', 'RLELossless'),  # noqa
    '1.2.840.10008.1.2.6.1': ('RFC 2557 MIME encapsulation', 'Transfer Syntax', '', 'Retired', 'RFC2557MIMEEncapsulation'),  # noqa
    '1.2.840.10008.1.2.6.2': ('XML Encoding', 'Transfer Syntax', '', 'Retired', 'XMLEncoding'),  # noqa
    '1.2.840.10008.1.2.7.1': ('SMPTE ST 2110-20 Uncompressed Progressive Active Video', 'Transfer Syntax', '', '', 'SMPTEST211020UncompressedProgressiveActiveVideo'),  # noqa
    '1.2.840.10008.1.2.7.2': ('SMPTE ST 2110-20 Uncompressed Interlaced Active Video', 'Transfer Syntax', '', '', 'SMPTEST211020UncompressedInterlacedActiveVideo'),  # noqa
    '1.2.840.10008.1.2.7.3': ('SMPTE ST 2110-30 PCM Digital Audio', 'Transfer Syntax', '', '', 'SMPTEST211030PCMDigitalAudio'),  # noqa
    '1.2.840.10008.1.3.10': ('Media Storage Directory Storage', 'SOP Class', '', '', 'MediaStorageDirectoryStorage'),  # noqa
    '1.2.840.10008.1.4.1.1': ('Talairach Brain Atlas Frame of Reference', 'Well-known frame of reference', '', '', 'TalairachBrainAtlas'),  # noqa
    '1.2.840.10008.1.4.1.2': ('SPM2 T1 Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2T1'),  # noqa
    '1.2.840.10008.1.4.1.3': ('SPM2 T2 Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2T2'),  # noqa
    '1.2.840.10008.1.4.1.4': ('SPM2 PD Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2PD'),  # noqa
    '1.2.840.10008.1.4.1.5': ('SPM2 EPI Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2EPI'),  # noqa
    '1.2.840.10008.1.4.1.6': ('SPM2 FIL T1 Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2FILT1'),  # noqa
    '1.2.840.10008.1.4.1.7': ('SPM2 PET Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2PET'),  # noqa
    '1.2.840.10008.1.4.1.8': ('SPM2 TRANSM Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2TRANSM'),  # noqa
    '1.2.840.10008.1.4.1.9': ('SPM2 SPECT Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2SPECT'),  # noqa
    '1.2.840.10008.1.4.1.10': ('SPM2 GRAY Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2GRAY'),  # noqa
    '1.2.840.10008.1.4.1.11': ('SPM2 WHITE Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2WHITE'),  # noqa
    '1.2.840.10008.1.4.1.12': ('SPM2 CSF Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2CSF'),  # noqa
    '1.2.840.10008.1.4.1.13': ('SPM2 BRAINMASK Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2BRAINMASK'),  # noqa
    '1.2.840.10008.1.4.1.14': ('SPM2 AVG305T1 Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2AVG305T1'),  # noqa
    '1.2.840.10008.1.4.1.15': ('SPM2 AVG152T1 Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2AVG152T1'),  # noqa
    '1.2.840.10008.1.4.1.16': ('SPM2 AVG152T2 Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2AVG152T2'),  # noqa
    '1.2.840.10008.1.4.1.17': ('SPM2 AVG152PD Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2AVG152PD'),  # noqa
    '1.2.840.10008.1.4.1.18': ('SPM2 SINGLESUBJT1 Frame of Reference', 'Well-known frame of reference', '', '', 'SPM2SINGLESUBJT1'),  # noqa
    '1.2.840.10008.1.4.2.1': ('ICBM 452 T1 Frame of Reference', 'Well-known frame of reference', '', '', 'ICBM452T1'),  # noqa
    '1.2.840.10008.1.4.2.2': ('ICBM Single Subject MRI Frame of Reference', 'Well-known frame of reference', '', '', 'ICBMSingleSubjectMRI'),  # noqa
    '1.2.840.10008.1.4.3.1': ('IEC 61217 Fixed Coordinate System Frame of Reference', 'Well-known frame of reference', '', '', 'IEC61217FixedCoordinateSystem'),  # noqa
    '1.2.840.10008.1.4.3.2': ('Standard Robotic-Arm Coordinate System Frame of Reference', 'Well-known frame of reference', '', '', 'StandardRoboticArmCoordinateSystem'),  # noqa
    '1.2.840.10008.1.4.4.1': ('SRI24 Frame of Reference', 'Well-known frame of reference', '', '', 'SRI24'),  # noqa
    '1.2.840.10008.1.4.5.1': ('Colin27 Frame of Reference', 'Well-known frame of reference', '', '', 'Colin27'),  # noqa
    '1.2.840.10008.1.4.6.1': ('LPBA40/AIR Frame of Reference', 'Well-known frame of reference', '', '', 'LPBA40AIR'),  # noqa
    '1.2.840.10008.1.4.6.2': ('LPBA40/FLIRT Frame of Reference', 'Well-known frame of reference', '', '', 'LPBA40FLIRT'),  # noqa
    '1.2.840.10008.1.4.6.3': ('LPBA40/SPM5 Frame of Reference', 'Well-known frame of reference', '', '', 'LPBA40SPM5'),  # noqa
    '1.2.840.10008.1.5.1': ('Hot Iron Color Palette SOP Instance', 'Well-known SOP Instance', '', '', 'HotIronPalette'),  # noqa
    '1.2.840.10008.1.5.2': ('PET Color Palette SOP Instance', 'Well-known SOP Instance', '', '', 'PETPalette'),  # noqa
    '1.2.840.10008.1.5.3': ('Hot Metal Blue Color Palette SOP Instance', 'Well-known SOP Instance', '', '', 'HotMetalBluePalette'),  # noqa
    '1.2.840.10008.1.5.4': ('PET 20 Step Color Palette SOP Instance', 'Well-known SOP Instance', '', '', 'PET20StepPalette'),  # noqa
    '1.2.840.10008.1.5.5': ('Spring Color Palette SOP Instance', 'Well-known SOP Instance', '', '', 'SpringPalette'),  # noqa
    '1.2.840.10008.1.5.6': ('Summer Color Palette SOP Instance', 'Well-known SOP Instance', '', '', 'SummerPalette'),  # noqa
    '1.2.840.10008.1.5.7': ('Fall Color Palette SOP Instance', 'Well-known SOP Instance', '', '', 'FallPalette'),  # noqa
    '1.2.840.10008.1.5.8': ('Winter Color Palette SOP Instance', 'Well-known SOP Instance', '', '', 'WinterPalette'),  # noqa
    '1.2.840.10008.1.9': ('Basic Study Content Notification SOP Class', 'SOP Class', '', 'Retired', 'BasicStudyContentNotification'),  # noqa
    '1.2.840.10008.1.20': ('Papyrus 3 Implicit VR Little Endian', 'Transfer Syntax', '(2015c)', 'Retired', 'Papyrus3ImplicitVRLittleEndian'),  # noqa
    '1.2.840.10008.1.20.1': ('Storage Commitment Push Model SOP Class', 'SOP Class', '', '', 'StorageCommitmentPushModel'),  # noqa
    '1.2.840.10008.1.20.1.1': ('Storage Commitment Push Model SOP Instance', 'Well-known SOP Instance', '', '', 'StorageCommitmentPushModelInstance'),  # noqa
    '1.2.840.10008.1.20.2': ('Storage Commitment Pull Model SOP Class', 'SOP Class', '', 'Retired', 'StorageCommitmentPullModel'),  # noqa
    '1.2.840.10008.1.20.2.1': ('Storage Commitment Pull Model SOP Instance', 'Well-known SOP Instance', '', 'Retired', 'StorageCommitmentPullModelInstance'),  # noqa
    '1.2.840.10008.1.40': ('Procedural Event Logging SOP Class', 'SOP Class', '', '', 'ProceduralEventLogging'),  # noqa
    '1.2.840.10008.1.40.1': ('Procedural Event Logging SOP Instance', 'Well-known SOP Instance', '', '', 'ProceduralEventLoggingInstance'),  # noqa
    '1.2.840.10008.1.42': ('Substance Administration Logging SOP Class', 'SOP Class', '', '', 'SubstanceAdministrationLogging'),  # noqa
    '1.2.840.10008.1.42.1': ('Substance Administration Logging SOP Instance', 'Well-known SOP Instance', '', '', 'SubstanceAdministrationLoggingInstance'),  # noqa
    '1.2.840.10008.2.6.1': ('DICOM UID Registry', 'DICOM UIDs as a Coding Scheme', '', '', 'DCMUID'),  # noqa
    '1.2.840.10008.2.16.4': ('DICOM Controlled Terminology', 'Coding Scheme', '', '', 'DCM'),  # noqa
    '1.2.840.10008.2.16.5': ('Adult Mouse Anatomy Ontology', 'Coding Scheme', '', '', 'MA'),  # noqa
    '1.2.840.10008.2.16.6': ('Uberon Ontology', 'Coding Scheme', '', '', 'UBERON'),  # noqa
    '1.2.840.10008.2.16.7': ('Integrated Taxonomic Information System (ITIS) Taxonomic Serial Number (TSN)', 'Coding Scheme', '', '', 'ITIS_TSN'),  # noqa
    '1.2.840.10008.2.16.8': ('Mouse Genome Initiative (MGI)', 'Coding Scheme', '', '', 'MGI'),  # noqa
    '1.2.840.10008.2.16.9': ('PubChem Compound CID', 'Coding Scheme', '', '', 'PUBCHEM_CID'),  # noqa
    '1.2.840.10008.2.16.10': ('Dublin Core', 'Coding Scheme', '', '', 'DC'),  # noqa
    '1.2.840.10008.2.16.11': ('New York University Melanoma Clinical Cooperative Group', 'Coding Scheme', '', '', 'NYUMCCG'),  # noqa
    '1.2.840.10008.2.16.12': ('Mayo Clinic Non-radiological Images Specific Body Structure Anatomical Surface Region Guide', 'Coding Scheme', '', '', 'MAYONRISBSASRG'),  # noqa
    '1.2.840.10008.2.16.13': ('Image Biomarker Standardisation Initiative', 'Coding Scheme', '', '', 'IBSI'),  # noqa
    '1.2.840.10008.2.16.14': ('Radiomics Ontology', 'Coding Scheme', '', '', 'RO'),  # noqa
    '1.2.840.10008.2.16.15': ('RadElement', 'Coding Scheme', '', '', 'RADELEMENT'),  # noqa
    '1.2.840.10008.2.16.16': ('ICD-11', 'Coding Scheme', '', '', 'I11'),  # noqa
    '1.2.840.10008.3.1.1.1': ('DICOM Application Context Name', 'Application Context Name', '', '', 'DICOMApplicationContext'),  # noqa
    '1.2.840.10008.3.1.2.1.1': ('Detached Patient Management SOP Class', 'SOP Class', '', 'Retired', 'DetachedPatientManagement'),  # noqa
    '1.2.840.10008.3.1.2.1.4': ('Detached Patient Management Meta SOP Class', 'Meta SOP Class', '', 'Retired', 'DetachedPatientManagementMeta'),  # noqa
    '1.2.840.10008.3.1.2.2.1': ('Detached Visit Management SOP Class', 'SOP Class', '', 'Retired', 'DetachedVisitManagement'),  # noqa
    '1.2.840.10008.3.1.2.3.1': ('Detached Study Management SOP Class', 'SOP Class', '', 'Retired', 'DetachedStudyManagement'),  # noqa
    '1.2.840.10008.3.1.2.3.2': ('Study Component Management SOP Class', 'SOP Class', '', 'Retired', 'StudyComponentManagement'),  # noqa
    '1.2.840.10008.3.1.2.3.3': ('Modality Performed Procedure Step SOP Class', 'SOP Class', '', '', 'ModalityPerformedProcedureStep'),  # noqa
    '1.2.840.10008.3.1.2.3.4': ('Modality Performed Procedure Step Retrieve SOP Class', 'SOP Class', '', '', 'ModalityPerformedProcedureStepRetrieve'),  # noqa
    '1.2.840.10008.3.1.2.3.5': ('Modality Performed Procedure Step Notification SOP Class', 'SOP Class', '', '', 'ModalityPerformedProcedureStepNotification'),  # noqa
    '1.2.840.10008.3.1.2.5.1': ('Detached Results Management SOP Class', 'SOP Class', '', 'Retired', 'DetachedResultsManagement'),  # noqa
    '1.2.840.10008.3.1.2.5.4': ('Detached Results Management Meta SOP Class', 'Meta SOP Class', '', 'Retired', 'DetachedResultsManagementMeta'),  # noqa
    '1.2.840.10008.3.1.2.5.5': ('Detached Study Management Meta SOP Class', 'Meta SOP Class', '', 'Retired', 'DetachedStudyManagementMeta'),  # noqa
    '1.2.840.10008.3.1.2.6.1': ('Detached Interpretation Management SOP Class', 'SOP Class', '', 'Retired', 'DetachedInterpretationManagement'),  # noqa
    '1.2.840.10008.4.2': ('Storage Service Class', 'Service Class', '', '', 'Storage'),  # noqa
    '1.2.840.10008.5.1.1.1': ('Basic Film Session SOP Class', 'SOP Class', '', '', 'BasicFilmSession'),  # noqa
    '1.2.840.10008.5.1.1.2': ('Basic Film Box SOP Class', 'SOP Class', '', '', 'BasicFilmBox'),  # noqa
    '1.2.840.10008.5.1.1.4': ('Basic Grayscale Image Box SOP Class', 'SOP Class', '', '', 'BasicGrayscaleImageBox'),  # noqa
    '1.2.840.10008.5.1.1.4.1': ('Basic Color Image Box SOP Class', 'SOP Class', '', '', 'BasicColorImageBox'),  # noqa
    '1.2.840.10008.5.1.1.4.2': ('Referenced Image Box SOP Class', 'SOP Class', '', 'Retired', 'ReferencedImageBox'),  # noqa
    '1.2.840.10008.5.1.1.9': ('Basic Grayscale Print Management Meta SOP Class', 'Meta SOP Class', '', '', 'BasicGrayscalePrintManagementMeta'),  # noqa
    '1.2.840.10008.5.1.1.9.1': ('Referenced Grayscale Print Management Meta SOP Class', 'Meta SOP Class', '', 'Retired', 'ReferencedGrayscalePrintManagementMeta'),  # noqa
    '1.2.840.10008.5.1.1.14': ('Print Job SOP Class', 'SOP Class', '', '', 'PrintJob'),  # noqa
    '1.2.840.10008.5.1.1.15': ('Basic Annotation Box SOP Class', 'SOP Class', '', '', 'BasicAnnotationBox'),  # noqa
    '1.2.840.10008.5.1.1.16': ('Printer SOP Class', 'SOP Class', '', '', 'Printer'),  # noqa
    '1.2.840.10008.5.1.1.16.376': ('Printer Configuration Retrieval SOP Class', 'SOP Class', '', '', 'PrinterConfigurationRetrieval'),  # noqa
    '1.2.840.10008.5.1.1.17': ('Printer SOP Instance', 'Well-known Printer SOP Instance', '', '', 'PrinterInstance'),  # noqa
    '1.2.840.10008.5.1.1.17.376': ('Printer Configuration Retrieval SOP Instance', 'Well-known Printer SOP Instance', '', '', 'PrinterConfigurationRetrievalInstance'),  # noqa
    '1.2.840.10008.5.1.1.18': ('Basic Color Print Management Meta SOP Class', 'Meta SOP Class', '', '', 'BasicColorPrintManagementMeta'),  # noqa
    '1.2.840.10008.5.1.1.18.1': ('Referenced Color Print Management Meta SOP Class', 'Meta SOP Class', '', 'Retired', 'ReferencedColorPrintManagementMeta'),  # noqa
    '1.2.840.10008.5.1.1.22': ('VOI LUT Box SOP Class', 'SOP Class', '', '', 'VOILUTBox'),  # noqa
    '1.2.840.10008.5.1.1.23': ('Presentation LUT SOP Class', 'SOP Class', '', '', 'PresentationLUT'),  # noqa
    '1.2.840.10008.5.1.1.24': ('Image Overlay Box SOP Class', 'SOP Class', '', 'Retired', 'ImageOverlayBox'),  # noqa
    '1.2.840.10008.5.1.1.24.1': ('Basic Print Image Overlay Box SOP Class', 'SOP Class', '', 'Retired', 'BasicPrintImageOverlayBox'),  # noqa
    '1.2.840.10008.5.1.1.25': ('Print Queue SOP Instance', 'Well-known Print Queue SOP Instance', '', 'Retired', 'PrintQueue'),  # noqa
    '1.2.840.10008.5.1.1.26': ('Print Queue Management SOP Class', 'SOP Class', '', 'Retired', 'PrintQueueManagement'),  # noqa
    '1.2.840.10008.5.1.1.27': ('Stored Print Storage SOP Class', 'SOP Class', '', 'Retired', 'StoredPrintStorage'),  # noqa
    '1.2.840.10008.5.1.1.29': ('Hardcopy Grayscale Image Storage SOP Class', 'SOP Class', '', 'Retired', 'HardcopyGrayscaleImageStorage'),  # noqa
    '1.2.840.10008.5.1.1.30': ('Hardcopy Color Image Storage SOP Class', 'SOP Class', '', 'Retired', 'HardcopyColorImageStorage'),  # noqa
    '1.2.840.10008.5.1.1.31': ('Pull Print Request SOP Class', 'SOP Class', '', 'Retired', 'PullPrintRequest'),  # noqa
    '1.2.840.10008.5.1.1.32': ('Pull Stored Print Management Meta SOP Class', 'Meta SOP Class', '', 'Retired', 'PullStoredPrintManagementMeta'),  # noqa
    '1.2.840.10008.5.1.1.33': ('Media Creation Management SOP Class UID', 'SOP Class', '', '', 'MediaCreationManagement'),  # noqa
    '1.2.840.10008.5.1.1.40': ('Display System SOP Class', 'SOP Class', '', '', 'DisplaySystem'),  # noqa
    '1.2.840.10008.5.1.1.40.1': ('Display System SOP Instance', 'Well-known SOP Instance', '', '', 'DisplaySystemInstance'),  # noqa
    '1.2.840.10008.5.1.4.1.1.1': ('Computed Radiography Image Storage', 'SOP Class', '', '', 'ComputedRadiographyImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.1.1': ('Digital X-Ray Image Storage - For Presentation', 'SOP Class', '', '', 'DigitalXRayImageStorageForPresentation'),  # noqa
    '1.2.840.10008.5.1.4.1.1.1.1.1': ('Digital X-Ray Image Storage - For Processing', 'SOP Class', '', '', 'DigitalXRayImageStorageForProcessing'),  # noqa
    '1.2.840.10008.5.1.4.1.1.1.2': ('Digital Mammography X-Ray Image Storage - For Presentation', 'SOP Class', '', '', 'DigitalMammographyXRayImageStorageForPresentation'),  # noqa
    '1.2.840.10008.5.1.4.1.1.1.2.1': ('Digital Mammography X-Ray Image Storage - For Processing', 'SOP Class', '', '', 'DigitalMammographyXRayImageStorageForProcessing'),  # noqa
    '1.2.840.10008.5.1.4.1.1.1.3': ('Digital Intra-Oral X-Ray Image Storage - For Presentation', 'SOP Class', '', '', 'DigitalIntraOralXRayImageStorageForPresentation'),  # noqa
    '1.2.840.10008.5.1.4.1.1.1.3.1': ('Digital Intra-Oral X-Ray Image Storage - For Processing', 'SOP Class', '', '', 'DigitalIntraOralXRayImageStorageForProcessing'),  # noqa
    '1.2.840.10008.5.1.4.1.1.2': ('CT Image Storage', 'SOP Class', '', '', 'CTImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.2.1': ('Enhanced CT Image Storage', 'SOP Class', '', '', 'EnhancedCTImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.2.2': ('Legacy Converted Enhanced CT Image Storage', 'SOP Class', '', '', 'LegacyConvertedEnhancedCTImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.3': ('Ultrasound Multi-frame Image Storage', 'SOP Class', '', 'Retired', 'UltrasoundMultiFrameImageStorageRetired'),  # noqa
    '1.2.840.10008.5.1.4.1.1.3.1': ('Ultrasound Multi-frame Image Storage', 'SOP Class', '', '', 'UltrasoundMultiFrameImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.4': ('MR Image Storage', 'SOP Class', '', '', 'MRImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.4.1': ('Enhanced MR Image Storage', 'SOP Class', '', '', 'EnhancedMRImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.4.2': ('MR Spectroscopy Storage', 'SOP Class', '', '', 'MRSpectroscopyStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.4.3': ('Enhanced MR Color Image Storage', 'SOP Class', '', '', 'EnhancedMRColorImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.4.4': ('Legacy Converted Enhanced MR Image Storage', 'SOP Class', '', '', 'LegacyConvertedEnhancedMRImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.5': ('Nuclear Medicine Image Storage', 'SOP Class', '', 'Retired', 'NuclearMedicineImageStorageRetired'),  # noqa
    '1.2.840.10008.5.1.4.1.1.6': ('Ultrasound Image Storage', 'SOP Class', '', 'Retired', 'UltrasoundImageStorageRetired'),  # noqa
    '1.2.840.10008.5.1.4.1.1.6.1': ('Ultrasound Image Storage', 'SOP Class', '', '', 'UltrasoundImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.6.2': ('Enhanced US Volume Storage', 'SOP Class', '', '', 'EnhancedUSVolumeStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.7': ('Secondary Capture Image Storage', 'SOP Class', '', '', 'SecondaryCaptureImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.7.1': ('Multi-frame Single Bit Secondary Capture Image Storage', 'SOP Class', '', '', 'MultiFrameSingleBitSecondaryCaptureImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.7.2': ('Multi-frame Grayscale Byte Secondary Capture Image Storage', 'SOP Class', '', '', 'MultiFrameGrayscaleByteSecondaryCaptureImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.7.3': ('Multi-frame Grayscale Word Secondary Capture Image Storage', 'SOP Class', '', '', 'MultiFrameGrayscaleWordSecondaryCaptureImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.7.4': ('Multi-frame True Color Secondary Capture Image Storage', 'SOP Class', '', '', 'MultiFrameTrueColorSecondaryCaptureImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.8': ('Standalone Overlay Storage', 'SOP Class', '', 'Retired', 'StandaloneOverlayStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9': ('Standalone Curve Storage', 'SOP Class', '', 'Retired', 'StandaloneCurveStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.1': ('Waveform Storage - Trial', 'SOP Class', '', 'Retired', 'WaveformStorageTrial'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.1.1': ('12-lead ECG Waveform Storage', 'SOP Class', '', '', 'TwelveLeadECGWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.1.2': ('General ECG Waveform Storage', 'SOP Class', '', '', 'GeneralECGWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.1.3': ('Ambulatory ECG Waveform Storage', 'SOP Class', '', '', 'AmbulatoryECGWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.2.1': ('Hemodynamic Waveform Storage', 'SOP Class', '', '', 'HemodynamicWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.3.1': ('Cardiac Electrophysiology Waveform Storage', 'SOP Class', '', '', 'CardiacElectrophysiologyWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.4.1': ('Basic Voice Audio Waveform Storage', 'SOP Class', '', '', 'BasicVoiceAudioWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.4.2': ('General Audio Waveform Storage', 'SOP Class', '', '', 'GeneralAudioWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.5.1': ('Arterial Pulse Waveform Storage', 'SOP Class', '', '', 'ArterialPulseWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.6.1': ('Respiratory Waveform Storage', 'SOP Class', '', '', 'RespiratoryWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.6.2': ('Multi-channel Respiratory Waveform Storage', 'SOP Class', '', '', 'MultichannelRespiratoryWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.7.1': ('Routine Scalp Electroencephalogram Waveform Storage', 'SOP Class', '', '', 'RoutineScalpElectroencephalogramWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.7.2': ('Electromyogram Waveform Storage', 'SOP Class', '', '', 'ElectromyogramWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.7.3': ('Electrooculogram Waveform Storage', 'SOP Class', '', '', 'ElectrooculogramWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.7.4': ('Sleep Electroencephalogram Waveform Storage', 'SOP Class', '', '', 'SleepElectroencephalogramWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.9.8.1': ('Body Position Waveform Storage', 'SOP Class', '', '', 'BodyPositionWaveformStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.10': ('Standalone Modality LUT Storage', 'SOP Class', '', 'Retired', 'StandaloneModalityLUTStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11': ('Standalone VOI LUT Storage', 'SOP Class', '', 'Retired', 'StandaloneVOILUTStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.1': ('Grayscale Softcopy Presentation State Storage', 'SOP Class', '', '', 'GrayscaleSoftcopyPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.2': ('Color Softcopy Presentation State Storage', 'SOP Class', '', '', 'ColorSoftcopyPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.3': ('Pseudo-Color Softcopy Presentation State Storage', 'SOP Class', '', '', 'PseudoColorSoftcopyPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.4': ('Blending Softcopy Presentation State Storage', 'SOP Class', '', '', 'BlendingSoftcopyPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.5': ('XA/XRF Grayscale Softcopy Presentation State Storage', 'SOP Class', '', '', 'XAXRFGrayscaleSoftcopyPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.6': ('Grayscale Planar MPR Volumetric Presentation State Storage', 'SOP Class', '', '', 'GrayscalePlanarMPRVolumetricPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.7': ('Compositing Planar MPR Volumetric Presentation State Storage', 'SOP Class', '', '', 'CompositingPlanarMPRVolumetricPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.8': ('Advanced Blending Presentation State Storage', 'SOP Class', '', '', 'AdvancedBlendingPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.9': ('Volume Rendering Volumetric Presentation State Storage', 'SOP Class', '', '', 'VolumeRenderingVolumetricPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.10': ('Segmented Volume Rendering Volumetric Presentation State Storage', 'SOP Class', '', '', 'SegmentedVolumeRenderingVolumetricPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.11.11': ('Multiple Volume Rendering Volumetric Presentation State Storage', 'SOP Class', '', '', 'MultipleVolumeRenderingVolumetricPresentationStateStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.12.1': ('X-Ray Angiographic Image Storage', 'SOP Class', '', '', 'XRayAngiographicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.12.1.1': ('Enhanced XA Image Storage', 'SOP Class', '', '', 'EnhancedXAImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.12.2': ('X-Ray Radiofluoroscopic Image Storage', 'SOP Class', '', '', 'XRayRadiofluoroscopicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.12.2.1': ('Enhanced XRF Image Storage', 'SOP Class', '', '', 'EnhancedXRFImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.12.3': ('X-Ray Angiographic Bi-Plane Image Storage', 'SOP Class', '', 'Retired', 'XRayAngiographicBiPlaneImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.12.77': ('', 'SOP Class', '(2015c)', 'Retired', ''),  # noqa
    '1.2.840.10008.5.1.4.1.1.13.1.1': ('X-Ray 3D Angiographic Image Storage', 'SOP Class', '', '', 'XRay3DAngiographicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.13.1.2': ('X-Ray 3D Craniofacial Image Storage', 'SOP Class', '', '', 'XRay3DCraniofacialImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.13.1.3': ('Breast Tomosynthesis Image Storage', 'SOP Class', '', '', 'BreastTomosynthesisImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.13.1.4': ('Breast Projection X-Ray Image Storage - For Presentation', 'SOP Class', '', '', 'BreastProjectionXRayImageStorageForPresentation'),  # noqa
    '1.2.840.10008.5.1.4.1.1.13.1.5': ('Breast Projection X-Ray Image Storage - For Processing', 'SOP Class', '', '', 'BreastProjectionXRayImageStorageForProcessing'),  # noqa
    '1.2.840.10008.5.1.4.1.1.14.1': ('Intravascular Optical Coherence Tomography Image Storage - For Presentation', 'SOP Class', '', '', 'IntravascularOpticalCoherenceTomographyImageStorageForPresentation'),  # noqa
    '1.2.840.10008.5.1.4.1.1.14.2': ('Intravascular Optical Coherence Tomography Image Storage - For Processing', 'SOP Class', '', '', 'IntravascularOpticalCoherenceTomographyImageStorageForProcessing'),  # noqa
    '1.2.840.10008.5.1.4.1.1.20': ('Nuclear Medicine Image Storage', 'SOP Class', '', '', 'NuclearMedicineImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.30': ('Parametric Map Storage', 'SOP Class', '', '', 'ParametricMapStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.40': ('', 'SOP Class', '(2015c)', 'Retired', ''),  # noqa
    '1.2.840.10008.5.1.4.1.1.66': ('Raw Data Storage', 'SOP Class', '', '', 'RawDataStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.66.1': ('Spatial Registration Storage', 'SOP Class', '', '', 'SpatialRegistrationStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.66.2': ('Spatial Fiducials Storage', 'SOP Class', '', '', 'SpatialFiducialsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.66.3': ('Deformable Spatial Registration Storage', 'SOP Class', '', '', 'DeformableSpatialRegistrationStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.66.4': ('Segmentation Storage', 'SOP Class', '', '', 'SegmentationStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.66.5': ('Surface Segmentation Storage', 'SOP Class', '', '', 'SurfaceSegmentationStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.66.6': ('Tractography Results Storage', 'SOP Class', '', '', 'TractographyResultsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.67': ('Real World Value Mapping Storage', 'SOP Class', '', '', 'RealWorldValueMappingStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.68.1': ('Surface Scan Mesh Storage', 'SOP Class', '', '', 'SurfaceScanMeshStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.68.2': ('Surface Scan Point Cloud Storage', 'SOP Class', '', '', 'SurfaceScanPointCloudStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1': ('VL Image Storage - Trial', 'SOP Class', '', 'Retired', 'VLImageStorageTrial'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.2': ('VL Multi-frame Image Storage - Trial', 'SOP Class', '', 'Retired', 'VLMultiFrameImageStorageTrial'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.1': ('VL Endoscopic Image Storage', 'SOP Class', '', '', 'VLEndoscopicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.1.1': ('Video Endoscopic Image Storage', 'SOP Class', '', '', 'VideoEndoscopicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.2': ('VL Microscopic Image Storage', 'SOP Class', '', '', 'VLMicroscopicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.2.1': ('Video Microscopic Image Storage', 'SOP Class', '', '', 'VideoMicroscopicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.3': ('VL Slide-Coordinates Microscopic Image Storage', 'SOP Class', '', '', 'VLSlideCoordinatesMicroscopicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.4': ('VL Photographic Image Storage', 'SOP Class', '', '', 'VLPhotographicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.4.1': ('Video Photographic Image Storage', 'SOP Class', '', '', 'VideoPhotographicImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.5.1': ('Ophthalmic Photography 8 Bit Image Storage', 'SOP Class', '', '', 'OphthalmicPhotography8BitImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.5.2': ('Ophthalmic Photography 16 Bit Image Storage', 'SOP Class', '', '', 'OphthalmicPhotography16BitImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.5.3': ('Stereometric Relationship Storage', 'SOP Class', '', '', 'StereometricRelationshipStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.5.4': ('Ophthalmic Tomography Image Storage', 'SOP Class', '', '', 'OphthalmicTomographyImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.5.5': ('Wide Field Ophthalmic Photography Stereographic Projection Image Storage', 'SOP Class', '', '', 'WideFieldOphthalmicPhotographyStereographicProjectionImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.5.6': ('Wide Field Ophthalmic Photography 3D Coordinates Image Storage', 'SOP Class', '', '', 'WideFieldOphthalmicPhotography3DCoordinatesImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.5.7': ('Ophthalmic Optical Coherence Tomography En Face Image Storage', 'SOP Class', '', '', 'OphthalmicOpticalCoherenceTomographyEnFaceImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.5.8': ('Ophthalmic Optical Coherence Tomography B-scan Volume Analysis Storage', 'SOP Class', '', '', 'OphthalmicOpticalCoherenceTomographyBscanVolumeAnalysisStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.77.1.6': ('VL Whole Slide Microscopy Image Storage', 'SOP Class', '', '', 'VLWholeSlideMicroscopyImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.78.1': ('Lensometry Measurements Storage', 'SOP Class', '', '', 'LensometryMeasurementsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.78.2': ('Autorefraction Measurements Storage', 'SOP Class', '', '', 'AutorefractionMeasurementsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.78.3': ('Keratometry Measurements Storage', 'SOP Class', '', '', 'KeratometryMeasurementsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.78.4': ('Subjective Refraction Measurements Storage', 'SOP Class', '', '', 'SubjectiveRefractionMeasurementsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.78.5': ('Visual Acuity Measurements Storage', 'SOP Class', '', '', 'VisualAcuityMeasurementsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.78.6': ('Spectacle Prescription Report Storage', 'SOP Class', '', '', 'SpectaclePrescriptionReportStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.78.7': ('Ophthalmic Axial Measurements Storage', 'SOP Class', '', '', 'OphthalmicAxialMeasurementsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.78.8': ('Intraocular Lens Calculations Storage', 'SOP Class', '', '', 'IntraocularLensCalculationsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.79.1': ('Macular Grid Thickness and Volume Report Storage', 'SOP Class', '', '', 'MacularGridThicknessAndVolumeReportStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.80.1': ('Ophthalmic Visual Field Static Perimetry Measurements Storage', 'SOP Class', '', '', 'OphthalmicVisualFieldStaticPerimetryMeasurementsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.81.1': ('Ophthalmic Thickness Map Storage', 'SOP Class', '', '', 'OphthalmicThicknessMapStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.82.1': ('Corneal Topography Map Storage', 'SOP Class', '', '', 'CornealTopographyMapStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.1': ('Text SR Storage - Trial', 'SOP Class', '', 'Retired', 'TextSRStorageTrial'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.2': ('Audio SR Storage - Trial', 'SOP Class', '', 'Retired', 'AudioSRStorageTrial'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.3': ('Detail SR Storage - Trial', 'SOP Class', '', 'Retired', 'DetailSRStorageTrial'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.4': ('Comprehensive SR Storage - Trial', 'SOP Class', '', 'Retired', 'ComprehensiveSRStorageTrial'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.11': ('Basic Text SR Storage', 'SOP Class', '', '', 'BasicTextSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.22': ('Enhanced SR Storage', 'SOP Class', '', '', 'EnhancedSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.33': ('Comprehensive SR Storage', 'SOP Class', '', '', 'ComprehensiveSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.34': ('Comprehensive 3D SR Storage', 'SOP Class', '', '', 'Comprehensive3DSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.35': ('Extensible SR Storage', 'SOP Class', '', '', 'ExtensibleSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.40': ('Procedure Log Storage', 'SOP Class', '', '', 'ProcedureLogStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.50': ('Mammography CAD SR Storage', 'SOP Class', '', '', 'MammographyCADSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.59': ('Key Object Selection Document Storage', 'SOP Class', '', '', 'KeyObjectSelectionDocumentStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.65': ('Chest CAD SR Storage', 'SOP Class', '', '', 'ChestCADSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.67': ('X-Ray Radiation Dose SR Storage', 'SOP Class', '', '', 'XRayRadiationDoseSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.68': ('Radiopharmaceutical Radiation Dose SR Storage', 'SOP Class', '', '', 'RadiopharmaceuticalRadiationDoseSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.69': ('Colon CAD SR Storage', 'SOP Class', '', '', 'ColonCADSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.70': ('Implantation Plan SR Storage', 'SOP Class', '', '', 'ImplantationPlanSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.71': ('Acquisition Context SR Storage', 'SOP Class', '', '', 'AcquisitionContextSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.72': ('Simplified Adult Echo SR Storage', 'SOP Class', '', '', 'SimplifiedAdultEchoSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.73': ('Patient Radiation Dose SR Storage', 'SOP Class', '', '', 'PatientRadiationDoseSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.74': ('Planned Imaging Agent Administration SR Storage', 'SOP Class', '', '', 'PlannedImagingAgentAdministrationSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.88.75': ('Performed Imaging Agent Administration SR Storage', 'SOP Class', '', '', 'PerformedImagingAgentAdministrationSRStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.90.1': ('Content Assessment Results Storage', 'SOP Class', '', '', 'ContentAssessmentResultsStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.104.1': ('Encapsulated PDF Storage', 'SOP Class', '', '', 'EncapsulatedPDFStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.104.2': ('Encapsulated CDA Storage', 'SOP Class', '', '', 'EncapsulatedCDAStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.104.3': ('Encapsulated STL Storage', 'SOP Class', '', '', 'EncapsulatedSTLStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.104.4': ('Encapsulated OBJ Storage', 'SOP Class', '', '', 'EncapsulatedOBJStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.104.5': ('Encapsulated MTL Storage', 'SOP Class', '', '', 'EncapsulatedMTLStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.128': ('Positron Emission Tomography Image Storage', 'SOP Class', '', '', 'PositronEmissionTomographyImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.128.1': ('Legacy Converted Enhanced PET Image Storage', 'SOP Class', '', '', 'LegacyConvertedEnhancedPETImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.129': ('Standalone PET Curve Storage', 'SOP Class', '', 'Retired', 'StandalonePETCurveStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.130': ('Enhanced PET Image Storage', 'SOP Class', '', '', 'EnhancedPETImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.131': ('Basic Structured Display Storage', 'SOP Class', '', '', 'BasicStructuredDisplayStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.200.1': ('CT Defined Procedure Protocol Storage', 'SOP Class', '', '', 'CTDefinedProcedureProtocolStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.200.2': ('CT Performed Procedure Protocol Storage', 'SOP Class', '', '', 'CTPerformedProcedureProtocolStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.200.3': ('Protocol Approval Storage', 'SOP Class', '', '', 'ProtocolApprovalStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.200.4': ('Protocol Approval Information Model - FIND', 'SOP Class', '', '', 'ProtocolApprovalInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.1.1.200.5': ('Protocol Approval Information Model - MOVE', 'SOP Class', '', '', 'ProtocolApprovalInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.1.1.200.6': ('Protocol Approval Information Model - GET', 'SOP Class', '', '', 'ProtocolApprovalInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.1': ('RT Image Storage', 'SOP Class', '', '', 'RTImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.2': ('RT Dose Storage', 'SOP Class', '', '', 'RTDoseStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.3': ('RT Structure Set Storage', 'SOP Class', '', '', 'RTStructureSetStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.4': ('RT Beams Treatment Record Storage', 'SOP Class', '', '', 'RTBeamsTreatmentRecordStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.5': ('RT Plan Storage', 'SOP Class', '', '', 'RTPlanStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.6': ('RT Brachy Treatment Record Storage', 'SOP Class', '', '', 'RTBrachyTreatmentRecordStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.7': ('RT Treatment Summary Record Storage', 'SOP Class', '', '', 'RTTreatmentSummaryRecordStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.8': ('RT Ion Plan Storage', 'SOP Class', '', '', 'RTIonPlanStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.9': ('RT Ion Beams Treatment Record Storage', 'SOP Class', '', '', 'RTIonBeamsTreatmentRecordStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.10': ('RT Physician Intent Storage', 'SOP Class', '', '', 'RTPhysicianIntentStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.11': ('RT Segment Annotation Storage', 'SOP Class', '', '', 'RTSegmentAnnotationStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.12': ('RT Radiation Set Storage', 'SOP Class', '', '', 'RTRadiationSetStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.13': ('C-Arm Photon-Electron Radiation Storage', 'SOP Class', '', '', 'CArmPhotonElectronRadiationStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.14': ('Tomotherapeutic Radiation Storage', 'SOP Class', '', '', 'TomotherapeuticRadiationStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.15': ('Robotic-Arm Radiation Storage', 'SOP Class', '', '', 'RoboticArmRadiationStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.16': ('RT Radiation Record Set Storage', 'SOP Class', '', '', 'RTRadiationRecordSetStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.17': ('RT Radiation Salvage Record Storage', 'SOP Class', '', '', 'RTRadiationSalvageRecordStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.18': ('Tomotherapeutic Radiation Record Storage', 'SOP Class', '', '', 'TomotherapeuticRadiationRecordStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.19': ('C-Arm Photon-Electron Radiation Record Storage', 'SOP Class', '', '', 'CArmPhotonElectronRadiationRecordStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.481.20': ('Robotic Radiation Record Storage', 'SOP Class', '', '', 'RoboticRadiationRecordStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.501.1': ('DICOS CT Image Storage', 'SOP Class', 'DICOS', '', 'DICOSCTImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.501.2.1': ('DICOS Digital X-Ray Image Storage - For Presentation', 'SOP Class', 'DICOS', '', 'DICOSDigitalXRayImageStorageForPresentation'),  # noqa
    '1.2.840.10008.5.1.4.1.1.501.2.2': ('DICOS Digital X-Ray Image Storage - For Processing', 'SOP Class', 'DICOS', '', 'DICOSDigitalXRayImageStorageForProcessing'),  # noqa
    '1.2.840.10008.5.1.4.1.1.501.3': ('DICOS Threat Detection Report Storage', 'SOP Class', 'DICOS', '', 'DICOSThreatDetectionReportStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.501.4': ('DICOS 2D AIT Storage', 'SOP Class', 'DICOS', '', 'DICOS2DAITStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.501.5': ('DICOS 3D AIT Storage', 'SOP Class', 'DICOS', '', 'DICOS3DAITStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.501.6': ('DICOS Quadrupole Resonance (QR) Storage', 'SOP Class', 'DICOS', '', 'DICOSQuadrupoleResonanceStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.601.1': ('Eddy Current Image Storage', 'SOP Class', 'DICONDE ASTM E2934', '', 'EddyCurrentImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.1.601.2': ('Eddy Current Multi-frame Image Storage', 'SOP Class', 'DICONDE ASTM E2934', '', 'EddyCurrentMultiFrameImageStorage'),  # noqa
    '1.2.840.10008.5.1.4.1.2.1.1': ('Patient Root Query/Retrieve Information Model - FIND', 'SOP Class', '', '', 'PatientRootQueryRetrieveInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.1.2.1.2': ('Patient Root Query/Retrieve Information Model - MOVE', 'SOP Class', '', '', 'PatientRootQueryRetrieveInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.1.2.1.3': ('Patient Root Query/Retrieve Information Model - GET', 'SOP Class', '', '', 'PatientRootQueryRetrieveInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.1.2.2.1': ('Study Root Query/Retrieve Information Model - FIND', 'SOP Class', '', '', 'StudyRootQueryRetrieveInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.1.2.2.2': ('Study Root Query/Retrieve Information Model - MOVE', 'SOP Class', '', '', 'StudyRootQueryRetrieveInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.1.2.2.3': ('Study Root Query/Retrieve Information Model - GET', 'SOP Class', '', '', 'StudyRootQueryRetrieveInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.1.2.3.1': ('Patient/Study Only Query/Retrieve Information Model - FIND', 'SOP Class', '', 'Retired', 'PatientStudyOnlyQueryRetrieveInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.1.2.3.2': ('Patient/Study Only Query/Retrieve Information Model - MOVE', 'SOP Class', '', 'Retired', 'PatientStudyOnlyQueryRetrieveInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.1.2.3.3': ('Patient/Study Only Query/Retrieve Information Model - GET', 'SOP Class', '', 'Retired', 'PatientStudyOnlyQueryRetrieveInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.1.2.4.2': ('Composite Instance Root Retrieve - MOVE', 'SOP Class', '', '', 'CompositeInstanceRootRetrieveMove'),  # noqa
    '1.2.840.10008.5.1.4.1.2.4.3': ('Composite Instance Root Retrieve - GET', 'SOP Class', '', '', 'CompositeInstanceRootRetrieveGet'),  # noqa
    '1.2.840.10008.5.1.4.1.2.5.3': ('Composite Instance Retrieve Without Bulk Data - GET', 'SOP Class', '', '', 'CompositeInstanceRetrieveWithoutBulkDataGet'),  # noqa
    '1.2.840.10008.5.1.4.20.1': ('Defined Procedure Protocol Information Model - FIND', 'SOP Class', '', '', 'DefinedProcedureProtocolInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.20.2': ('Defined Procedure Protocol Information Model - MOVE', 'SOP Class', '', '', 'DefinedProcedureProtocolInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.20.3': ('Defined Procedure Protocol Information Model - GET', 'SOP Class', '', '', 'DefinedProcedureProtocolInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.31': ('Modality Worklist Information Model - FIND', 'SOP Class', '', '', 'ModalityWorklistInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.32': ('General Purpose Worklist Management Meta SOP Class', 'Meta SOP Class', '', 'Retired', 'GeneralPurposeWorklistManagementMeta'),  # noqa
    '1.2.840.10008.5.1.4.32.1': ('General Purpose Worklist Information Model - FIND', 'SOP Class', '', 'Retired', 'GeneralPurposeWorklistInformationModelFIND'),  # noqa
    '1.2.840.10008.5.1.4.32.2': ('General Purpose Scheduled Procedure Step SOP Class', 'SOP Class', '', 'Retired', 'GeneralPurposeScheduledProcedureStep'),  # noqa
    '1.2.840.10008.5.1.4.32.3': ('General Purpose Performed Procedure Step SOP Class', 'SOP Class', '', 'Retired', 'GeneralPurposePerformedProcedureStep'),  # noqa
    '1.2.840.10008.5.1.4.33': ('Instance Availability Notification SOP Class', 'SOP Class', '', '', 'InstanceAvailabilityNotification'),  # noqa
    '1.2.840.10008.5.1.4.34.1': ('RT Beams Delivery Instruction Storage - Trial', 'SOP Class', '', 'Retired', 'RTBeamsDeliveryInstructionStorageTrial'),  # noqa
    '1.2.840.10008.5.1.4.34.2': ('RT Conventional Machine Verification - Trial', 'SOP Class', '', 'Retired', 'RTConventionalMachineVerificationTrial'),  # noqa
    '1.2.840.10008.5.1.4.34.3': ('RT Ion Machine Verification - Trial', 'SOP Class', '', 'Retired', 'RTIonMachineVerificationTrial'),  # noqa
    '1.2.840.10008.5.1.4.34.4': ('Unified Worklist and Procedure Step Service Class - Trial', 'Service Class', '', 'Retired', 'UnifiedWorklistAndProcedureStepTrial'),  # noqa
    '1.2.840.10008.5.1.4.34.4.1': ('Unified Procedure Step - Push SOP Class - Trial', 'SOP Class', '', 'Retired', 'UnifiedProcedureStepPushTrial'),  # noqa
    '1.2.840.10008.5.1.4.34.4.2': ('Unified Procedure Step - Watch SOP Class - Trial', 'SOP Class', '', 'Retired', 'UnifiedProcedureStepWatchTrial'),  # noqa
    '1.2.840.10008.5.1.4.34.4.3': ('Unified Procedure Step - Pull SOP Class - Trial', 'SOP Class', '', 'Retired', 'UnifiedProcedureStepPullTrial'),  # noqa
    '1.2.840.10008.5.1.4.34.4.4': ('Unified Procedure Step - Event SOP Class - Trial', 'SOP Class', '', 'Retired', 'UnifiedProcedureStepEventTrial'),  # noqa
    '1.2.840.10008.5.1.4.34.5': ('UPS Global Subscription SOP Instance', 'Well-known SOP Instance', '', '', 'UPSGlobalSubscriptionInstance'),  # noqa
    '1.2.840.10008.5.1.4.34.5.1': ('UPS Filtered Global Subscription SOP Instance', 'Well-known SOP Instance', '', '', 'UPSFilteredGlobalSubscriptionInstance'),  # noqa
    '1.2.840.10008.5.1.4.34.6': ('Unified Worklist and Procedure Step Service Class', 'Service Class', '', '', 'UnifiedWorklistAndProcedureStep'),  # noqa
    '1.2.840.10008.5.1.4.34.6.1': ('Unified Procedure Step - Push SOP Class', 'SOP Class', '', '', 'UnifiedProcedureStepPush'),  # noqa
    '1.2.840.10008.5.1.4.34.6.2': ('Unified Procedure Step - Watch SOP Class', 'SOP Class', '', '', 'UnifiedProcedureStepWatch'),  # noqa
    '1.2.840.10008.5.1.4.34.6.3': ('Unified Procedure Step - Pull SOP Class', 'SOP Class', '', '', 'UnifiedProcedureStepPull'),  # noqa
    '1.2.840.10008.5.1.4.34.6.4': ('Unified Procedure Step - Event SOP Class', 'SOP Class', '', '', 'UnifiedProcedureStepEvent'),  # noqa
    '1.2.840.10008.5.1.4.34.6.5': ('Unified Procedure Step - Query SOP Class', 'SOP Class', '', '', 'UnifiedProcedureStepQuery'),  # noqa
    '1.2.840.10008.5.1.4.34.7': ('RT Beams Delivery Instruction Storage', 'SOP Class', '', '', 'RTBeamsDeliveryInstructionStorage'),  # noqa
    '1.2.840.10008.5.1.4.34.8': ('RT Conventional Machine Verification', 'SOP Class', '', '', 'RTConventionalMachineVerification'),  # noqa
    '1.2.840.10008.5.1.4.34.9': ('RT Ion Machine Verification', 'SOP Class', '', '', 'RTIonMachineVerification'),  # noqa
    '1.2.840.10008.5.1.4.34.10': ('RT Brachy Application Setup Delivery Instruction Storage', 'SOP Class', '', '', 'RTBrachyApplicationSetupDeliveryInstructionStorage'),  # noqa
    '1.2.840.10008.5.1.4.37.1': ('General Relevant Patient Information Query', 'SOP Class', '', '', 'GeneralRelevantPatientInformationQuery'),  # noqa
    '1.2.840.10008.5.1.4.37.2': ('Breast Imaging Relevant Patient Information Query', 'SOP Class', '', '', 'BreastImagingRelevantPatientInformationQuery'),  # noqa
    '1.2.840.10008.5.1.4.37.3': ('Cardiac Relevant Patient Information Query', 'SOP Class', '', '', 'CardiacRelevantPatientInformationQuery'),  # noqa
    '1.2.840.10008.5.1.4.38.1': ('Hanging Protocol Storage', 'SOP Class', '', '', 'HangingProtocolStorage'),  # noqa
    '1.2.840.10008.5.1.4.38.2': ('Hanging Protocol Information Model - FIND', 'SOP Class', '', '', 'HangingProtocolInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.38.3': ('Hanging Protocol Information Model - MOVE', 'SOP Class', '', '', 'HangingProtocolInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.38.4': ('Hanging Protocol Information Model - GET', 'SOP Class', '', '', 'HangingProtocolInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.39.1': ('Color Palette Storage', 'SOP Class', '', '', 'ColorPaletteStorage'),  # noqa
    '1.2.840.10008.5.1.4.39.2': ('Color Palette Query/Retrieve Information Model - FIND', 'SOP Class', '', '', 'ColorPaletteQueryRetrieveInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.39.3': ('Color Palette Query/Retrieve Information Model - MOVE', 'SOP Class', '', '', 'ColorPaletteQueryRetrieveInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.39.4': ('Color Palette Query/Retrieve Information Model - GET', 'SOP Class', '', '', 'ColorPaletteQueryRetrieveInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.41': ('Product Characteristics Query SOP Class', 'SOP Class', '', '', 'ProductCharacteristicsQuery'),  # noqa
    '1.2.840.10008.5.1.4.42': ('Substance Approval Query SOP Class', 'SOP Class', '', '', 'SubstanceApprovalQuery'),  # noqa
    '1.2.840.10008.5.1.4.43.1': ('Generic Implant Template Storage', 'SOP Class', '', '', 'GenericImplantTemplateStorage'),  # noqa
    '1.2.840.10008.5.1.4.43.2': ('Generic Implant Template Information Model - FIND', 'SOP Class', '', '', 'GenericImplantTemplateInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.43.3': ('Generic Implant Template Information Model - MOVE', 'SOP Class', '', '', 'GenericImplantTemplateInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.43.4': ('Generic Implant Template Information Model - GET', 'SOP Class', '', '', 'GenericImplantTemplateInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.44.1': ('Implant Assembly Template Storage', 'SOP Class', '', '', 'ImplantAssemblyTemplateStorage'),  # noqa
    '1.2.840.10008.5.1.4.44.2': ('Implant Assembly Template Information Model - FIND', 'SOP Class', '', '', 'ImplantAssemblyTemplateInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.44.3': ('Implant Assembly Template Information Model - MOVE', 'SOP Class', '', '', 'ImplantAssemblyTemplateInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.44.4': ('Implant Assembly Template Information Model - GET', 'SOP Class', '', '', 'ImplantAssemblyTemplateInformationModelGet'),  # noqa
    '1.2.840.10008.5.1.4.45.1': ('Implant Template Group Storage', 'SOP Class', '', '', 'ImplantTemplateGroupStorage'),  # noqa
    '1.2.840.10008.5.1.4.45.2': ('Implant Template Group Information Model - FIND', 'SOP Class', '', '', 'ImplantTemplateGroupInformationModelFind'),  # noqa
    '1.2.840.10008.5.1.4.45.3': ('Implant Template Group Information Model - MOVE', 'SOP Class', '', '', 'ImplantTemplateGroupInformationModelMove'),  # noqa
    '1.2.840.10008.5.1.4.45.4': ('Implant Template Group Information Model - GET', 'SOP Class', '', '', 'ImplantTemplateGroupInformationModelGet'),  # noqa
    '1.2.840.10008.7.1.1': ('Native DICOM Model', 'Application Hosting Model', '', '', 'NativeDICOMModel'),  # noqa
    '1.2.840.10008.7.1.2': ('Abstract Multi-Dimensional Image Model', 'Application Hosting Model', '', '', 'AbstractMultiDimensionalImageModel'),  # noqa
    '1.2.840.10008.8.1.1': ('DICOM Content Mapping Resource', 'Mapping Resource', '', '', 'DICOMContentMappingResource'),  # noqa
    '1.2.840.10008.10.1': ('Video Endoscopic Image Real-Time Communication', 'SOP Class', '', '', 'VideoEndoscopicImageRealTimeCommunication'),  # noqa
    '1.2.840.10008.10.2': ('Video Photographic Image Real-Time Communication', 'SOP Class', '', '', 'VideoPhotographicImageRealTimeCommunication'),  # noqa
    '1.2.840.10008.10.3': ('Audio Waveform Real-Time Communication', 'SOP Class', '', '', 'AudioWaveformRealTimeCommunication'),  # noqa
    '1.2.840.10008.10.4': ('Rendition Selection Document Real-Time Communication', 'SOP Class', '', '', 'RenditionSelectionDocumentRealTimeCommunication'),  # noqa
    '1.2.840.10008.15.0.3.1': ('dicomDeviceName', 'LDAP OID', '', '', 'dicomDeviceName'),  # noqa
    '1.2.840.10008.15.0.3.2': ('dicomDescription', 'LDAP OID', '', '', 'dicomDescription'),  # noqa
    '1.2.840.10008.15.0.3.3': ('dicomManufacturer', 'LDAP OID', '', '', 'dicomManufacturer'),  # noqa
    '1.2.840.10008.15.0.3.4': ('dicomManufacturerModelName', 'LDAP OID', '', '', 'dicomManufacturerModelName'),  # noqa
    '1.2.840.10008.15.0.3.5': ('dicomSoftwareVersion', 'LDAP OID', '', '', 'dicomSoftwareVersion'),  # noqa
    '1.2.840.10008.15.0.3.6': ('dicomVendorData', 'LDAP OID', '', '', 'dicomVendorData'),  # noqa
    '1.2.840.10008.15.0.3.7': ('dicomAETitle', 'LDAP OID', '', '', 'dicomAETitle'),  # noqa
    '1.2.840.10008.15.0.3.8': ('dicomNetworkConnectionReference', 'LDAP OID', '', '', 'dicomNetworkConnectionReference'),  # noqa
    '1.2.840.10008.15.0.3.9': ('dicomApplicationCluster', 'LDAP OID', '', '', 'dicomApplicationCluster'),  # noqa
    '1.2.840.10008.15.0.3.10': ('dicomAssociationInitiator', 'LDAP OID', '', '', 'dicomAssociationInitiator'),  # noqa
    '1.2.840.10008.15.0.3.11': ('dicomAssociationAcceptor', 'LDAP OID', '', '', 'dicomAssociationAcceptor'),  # noqa
    '1.2.840.10008.15.0.3.12': ('dicomHostname', 'LDAP OID', '', '', 'dicomHostname'),  # noqa
    '1.2.840.10008.15.0.3.13': ('dicomPort', 'LDAP OID', '', '', 'dicomPort'),  # noqa
    '1.2.840.10008.15.0.3.14': ('dicomSOPClass', 'LDAP OID', '', '', 'dicomSOPClass'),  # noqa
    '1.2.840.10008.15.0.3.15': ('dicomTransferRole', 'LDAP OID', '', '', 'dicomTransferRole'),  # noqa
    '1.2.840.10008.15.0.3.16': ('dicomTransferSyntax', 'LDAP OID', '', '', 'dicomTransferSyntax'),  # noqa
    '1.2.840.10008.15.0.3.17': ('dicomPrimaryDeviceType', 'LDAP OID', '', '', 'dicomPrimaryDeviceType'),  # noqa
    '1.2.840.10008.15.0.3.18': ('dicomRelatedDeviceReference', 'LDAP OID', '', '', 'dicomRelatedDeviceReference'),  # noqa
    '1.2.840.10008.15.0.3.19': ('dicomPreferredCalledAETitle', 'LDAP OID', '', '', 'dicomPreferredCalledAETitle'),  # noqa
    '1.2.840.10008.15.0.3.20': ('dicomTLSCyphersuite', 'LDAP OID', '', '', 'dicomTLSCyphersuite'),  # noqa
    '1.2.840.10008.15.0.3.21': ('dicomAuthorizedNodeCertificateReference', 'LDAP OID', '', '', 'dicomAuthorizedNodeCertificateReference'),  # noqa
    '1.2.840.10008.15.0.3.22': ('dicomThisNodeCertificateReference', 'LDAP OID', '', '', 'dicomThisNodeCertificateReference'),  # noqa
    '1.2.840.10008.15.0.3.23': ('dicomInstalled', 'LDAP OID', '', '', 'dicomInstalled'),  # noqa
    '1.2.840.10008.15.0.3.24': ('dicomStationName', 'LDAP OID', '', '', 'dicomStationName'),  # noqa
    '1.2.840.10008.15.0.3.25': ('dicomDeviceSerialNumber', 'LDAP OID', '', '', 'dicomDeviceSerialNumber'),  # noqa
    '1.2.840.10008.15.0.3.26': ('dicomInstitutionName', 'LDAP OID', '', '', 'dicomInstitutionName'),  # noqa
    '1.2.840.10008.15.0.3.27': ('dicomInstitutionAddress', 'LDAP OID', '', '', 'dicomInstitutionAddress'),  # noqa
    '1.2.840.10008.15.0.3.28': ('dicomInstitutionDepartmentName', 'LDAP OID', '', '', 'dicomInstitutionDepartmentName'),  # noqa
    '1.2.840.10008.15.0.3.29': ('dicomIssuerOfPatientID', 'LDAP OID', '', '', 'dicomIssuerOfPatientID'),  # noqa
    '1.2.840.10008.15.0.3.30': ('dicomPreferredCallingAETitle', 'LDAP OID', '', '', 'dicomPreferredCallingAETitle'),  # noqa
    '1.2.840.10008.15.0.3.31': ('dicomSupportedCharacterSet', 'LDAP OID', '', '', 'dicomSupportedCharacterSet'),  # noqa
    '1.2.840.10008.15.0.4.1': ('dicomConfigurationRoot', 'LDAP OID', '', '', 'dicomConfigurationRoot'),  # noqa
    '1.2.840.10008.15.0.4.2': ('dicomDevicesRoot', 'LDAP OID', '', '', 'dicomDevicesRoot'),  # noqa
    '1.2.840.10008.15.0.4.3': ('dicomUniqueAETitlesRegistryRoot', 'LDAP OID', '', '', 'dicomUniqueAETitlesRegistryRoot'),  # noqa
    '1.2.840.10008.15.0.4.4': ('dicomDevice', 'LDAP OID', '', '', 'dicomDevice'),  # noqa
    '1.2.840.10008.15.0.4.5': ('dicomNetworkAE', 'LDAP OID', '', '', 'dicomNetworkAE'),  # noqa
    '1.2.840.10008.15.0.4.6': ('dicomNetworkConnection', 'LDAP OID', '', '', 'dicomNetworkConnection'),  # noqa
    '1.2.840.10008.15.0.4.7': ('dicomUniqueAETitle', 'LDAP OID', '', '', 'dicomUniqueAETitle'),  # noqa
    '1.2.840.10008.15.0.4.8': ('dicomTransferCapability', 'LDAP OID', '', '', 'dicomTransferCapability'),  # noqa
    '1.2.840.10008.15.1.1': ('Universal Coordinated Time', 'Synchronization Frame of Reference', '', '', 'UTC')  # noqa
}